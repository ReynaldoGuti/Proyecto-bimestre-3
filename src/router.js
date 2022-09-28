import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import Home from './components/Home.vue'
import LogIn from './components/LogIn.vue'
import SingUp from './components/SingUp.vue'
import Account from './components/Account.vue'

const routes = [{
path: '/',
name: 'root',
component: App
},
{
    path: '/user/logIn',
    name: "logIn",
    component: LogIn,
},
{
    path:'/user/account',
    name: "Account",
    component: Account,
},
{
    path: '/user/singUp',
    name: "singUp",
    component: SingUp,
},
{
    path: '/user/home',
    name: "Home",
    component: Home
}];

const router = createRouter({
history: createWebHistory(),
routes,
});

export default router;