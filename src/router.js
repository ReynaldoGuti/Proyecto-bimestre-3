import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import LogIn from './components/LogIn.vue'
import SingUp from './components/SingUp.vue'

const routes = [{
path: '/',
name: 'root',
component: App
},
{
    path: '/user/logIn',
    name: 'logIn',
    component: LogIn,
},
{
    path: '/user/singUp',
    name: 'singUp',
    component: SingUp,
}]

const router = createRouter({
history: createWebHistory(),
routes,
});

export default router