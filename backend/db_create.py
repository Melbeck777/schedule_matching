from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
import datetime
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///schedule_matching.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECREAT_KEY"] = os.urandom(24)

db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "User"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name       = db.Column(db.String(64))
    email      = db.Column(db.String(64))
    password   = db.Column(db.String(64))
    created_at = db.Column(db.DATE)

class Event(db.Model):
    __tablename__ = "Event"
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name     = db.Column(db.String(64))
    times    = db.Column(db.Integer)
    location = db.Column(db.String(64))
    owner_id = db.Column(db.Integer) # foreign key

class EventDuration(db.Model):
    __tablename__ = 'EventDuration'
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer)
    start    = db.Column(db.DATE)
    end      = db.Column(db.DATE)

class EventParticipate(db.Model):
    __tablename__ = 'EventParticipate'
    id        = db.Column(db.Integer, primary_key=True)
    event_id  = db.Column(db.Integer)
    user_mail = db.Column(db.Integer)

class UserSchedule(db.Model):
    __tablename__ = 'UserSchedule'
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name     = db.Column(db.String(64))
    location = db.Column(db.String(64))
    user_id  = db.Column(db.Integer) # foreign key
    start    = db.Column(db.DATE)
    end      = db.Column(db.DATE)    

db.init_app(app)
db.create_all()