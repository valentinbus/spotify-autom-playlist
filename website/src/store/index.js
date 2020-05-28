// store/index.js
 
import Vue from "vue";
import Vuex from "vuex";
 
Vue.use(Vuex);
 
export default new Vuex.Store({
    state: {
      connected: false,
      jwt_token: null,
      user_photo: null,
      user_id: null,
    },
    getters: {},
    mutations: {},
    actions: {}
   });