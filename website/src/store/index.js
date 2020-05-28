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

// function checkToken() {
//     let config = {
//         headers: {
//             jwt_token: this.$store.state.jwt_token
//         }
//     };
//     axios
//         .get("http://localhost:5000/check-token", config)
//         .then(
//             response => (
//                 (this.test = response),
//                 console.log("CHECK TOKEN:::" + response),
//                 this.test = cathError(response)
//             )
//         );
// }

// function cathError(response) {
//     if (response['data']["error"]) {
//         this.$store.state.connected = false
//         return "Vous devez vous connectez avant"
//     }
//     else {
//         return "ok"
//     }
// }