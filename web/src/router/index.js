import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home'
import Center from '../components/Centers'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Centers',
    name: 'Center',
    component: Center
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
