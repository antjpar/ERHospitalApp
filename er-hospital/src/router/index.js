import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard'
import WaitingRoom from '../views/WaitingRoom'
import CallCenter from '../views/CallCenter'
import EmergencyCenter from '../views/EmergencyCenter'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/waiting-room',
    name: 'WaitingRoom',
    component: WaitingRoom,
  },
  {
    path: '/call-center',
    name: 'CallCenter',
    component: CallCenter,
  },
  {
    path: '/emergency',
    name: 'EmergencyCenter',
    component: EmergencyCenter,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
