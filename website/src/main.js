import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'

Vue.use(VueSession)
Vue.config.productionTip = false
Vue.config.silent = true

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
