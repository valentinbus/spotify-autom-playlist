// store/index.js

import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        connected: false,
        jwt_token: null,
        user_photo: null,
        user_id: null,
        message_connection: null,
    },
    mutations: {},
    actions: {}
});

