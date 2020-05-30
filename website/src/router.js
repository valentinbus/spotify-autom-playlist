import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import Initialise from './views/Initialise.vue'
import Clear from './views/ClearDb.vue'
import Team from './views/Team.vue'
import CreatePlaylist from './views/CreatePlaylist'
import Connection from './views/Connection'
import LoginSuccess from './views/LoginSuccess'
import Test from './views/Test'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/init',
      name: 'init',
      component: Initialise
    },
    {
      path: '/clear',
      name: 'clear',
      component: Clear
    },
    {
      path: '/connection',
      name: 'connection',
      component: Connection
    },
    {
      path: '/login-success',
      name: 'loginsuccess',
      component: LoginSuccess
    },
    {
      path: '/team',
      name: 'team',
      component: Team
    },
    {
      path: '/createplaylist',
      name: 'createplaylist',
      component: CreatePlaylist
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    }

  ]
})
