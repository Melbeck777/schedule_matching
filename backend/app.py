import json
import os
from unicodedata import category, name
from weakref import ref 
from xml.etree.ElementPath import prepare_parent
from flask import Flask, render_template, jsonify
from flask import request, redirect, url_for
from flask_login import LoginManager, logout_user, login_required
from flask_cors import CORS
import datetime
from db_create import db
from db_create import User, Event, EventDuration, EventParticipate, UserSchedule
import subprocess

app = Flask(__name__, static_folder="../frontend/dist/static", template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule_matching.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.urandom(24)

CORS(app)

if os.path.exists('../backend/schedule_matching.db') == False:
    subprocess.run('py ./db_create.py')

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def index(path):
    print("Hello world")
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/signup',methods=['POST'])
def sign_in():
    post_data = request.get_json()
    today = datetime.datetime.now().date()
    new_user = User(name = post_data['name'],email = post_data['email'],
    password = post_data['password'],created_at = today)
    print("email = {}".format(post_data["email"]))
    print("name = {}".format(post_data["name"]))
    print("password = {}".format(post_data["password"]))
    db.session.add(new_user)
    db.session.commit()
    return redirect('/{}'.format(new_user.id))

@app.route('/login', methods=['POST'])
def login():
    post_data = request.get_json()
    user_data = db.session.query(User).filter(User.email == post_data['email']).first()
    user_password = user_data.password
    send_data = {'flag':False}
    if user_password == post_data['password']:
        send_data['flag'] = True
        send_data['id']   = user_data.id
    print("user_password = {}\npost_pass = {}".format(user_password, post_data['password']))
    print(send_data)
    return jsonify(send_data)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/event_create/<id>', methods=['POST'])
def event_create(id):
    post_data = request.get_json()
    
    # Register Event
    new_event = Event(name=post_data['name'],
        number=post_data['number'],
        location=post_data['location'],
        owner_id=id)
    db.session(new_event)
    db.commit()

    # Register EventDuration
    event_id = new_event.id
    for now_date in post_data['date']:
        event_duration = EventDuration(event_id=event_id,
                start=now_date['start'], end=now_date['end'])
        db.session(event_duration)
        db.commit()
    
    # Registration owner information
    if post_data['owner_mail'] == None:
        owner = EventParticipate(event_id=event_id, user_mail=db.query(User).filter(id=id).email)
        db.session(owner)
        db.commit()
    else:
        owner = EventParticipate(event_id=event_id, user_mail=post_data['owner_mail'])
        db.session(owner)
        db.commit()
    
    # Register all participation besides owner.
    for participate in post_data['participate']:
        event_participate = EventParticipate(event_id=id, user_mail=participate['email'])
        db.session(event_participate)
        db.commit()
    return jsonify({})

db.init_app(app)
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, use_debugger=True, use_reloader=True)
