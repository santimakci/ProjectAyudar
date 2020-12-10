import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home'
import Center from '../components/Centers'
import AddTurn from '../components/AddTurn'
import AddCenter from '../components/AddCenter'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/centers',
    name: 'Centers',
    component: Center 
  },
  {
    path: '/cargarCentro',
    name: 'addCenter',
    component: AddCenter 
  },
  {
    path: '/solicitarTurno/:center',
    name: 'solicitarTurno',
    component: AddTurn, 
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
