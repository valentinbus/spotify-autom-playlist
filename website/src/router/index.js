import Vue from 'vue'
import Router from 'vue-router'
import Presentation from '@/components/Presentation'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import Test from '@/components/Test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/presentation',
      name: 'Presentation',
      component: Presentation
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    },
    {
      path: '/header',
      name: 'Header',
      component: Header
    },
    {
      path: '/footer',
      name: 'Footer',
      component: Footer
    }
  ]
})
