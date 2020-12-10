import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home'
import Center from '../components/Centers'
import Turn from '../components/Turn'
import AddCenter from '../components/AddCenter'
import Statistics from '../components/Statistics'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/centros',
    name: 'Centers',
    component: Center 
  },
  {
    path: '/cargarCentro',
    name: 'addCenter',
    component: AddCenter 
  },
  {
    path: '/solicitarTurno',
    name: 'Turns',
    component: Turn 
  },
  {
    path: '/estadisticas',
    name: 'Statistics',
    component: Statistics 
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
