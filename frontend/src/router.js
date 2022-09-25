import Vue from 'vue'
import Router from 'vue-router'
import TopPage from './components/TopPage'
import SignIn from './components/SignIn'
import LogIn from './components/LogIn'
import CreateEvent from './components/CreateEvent'
import DateInput from './components/DateInput'
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
            path:'/create_event',
            name:'create_event',
            component:CreateEvent
        },
        {
            path:'/date_input',
            name:'date_input',
            component:DateInput
        }
    ]
})