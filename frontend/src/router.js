import Vue from 'vue'
import Router from 'vue-router'
import TopPage from './components/TopPage'
import SignIn from './components/SignIn'
import LogIn from './components/LogIn'
import CreateEvent from './components/CreateEvent'
import UserPage from './components/UserPage'
import GenreInput from './components/GenreInput'
import ShowEvent from './components/ShowEvent'

// import HelloWorld from './components/HelloWorld'

Vue.use(Router)

export default new Router({
    mode:'history',
    routes:[
        {
            path:'/',
            name:'top',
            component: TopPage
        },
        {
            path:'/sign_in',
            name:'sign_in',
            component:SignIn
        },
        {
            path:'/login',
            name:'login',
            component:LogIn
        },
        {
            path:'/user',
            name:'user',
            component:UserPage
        },
        {
            path:'/create_event',
            name:'create_event',
            component:CreateEvent
        },
        {
            path:'/add_genre',
            name:'add_genre',
            component:GenreInput
        },
        {
            path:'/show_event',
            name:'show_event',
            component:ShowEvent
        }
    ]
})