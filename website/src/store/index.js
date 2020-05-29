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
    },
    //check if token is valid
    getters: {
        checkToken: state => {
            let config = {
                headers: {
                    jwt_token: state.jwt_token
                }
            };
            axios
                .get("http://localhost:5000/check-token", config)
                .then(
                    response => (
                        cathError(response, state)
                    )
                );
            return state.connected
        },
    },
    mutations: {},
    actions: {}
});

function cathError(response, state) {
    if (response['data']["error"]) {
        state.connected = false
        return "You have to login before"
    }
    else {
        return "ok"
    }
}