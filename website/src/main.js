import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'
import store from "./store";

Vue.use(VueSession)
Vue.config.productionTip = false
Vue.config.silent = true

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
