<template>
    <v-row class="pa-4 text-center">
        <h1>Now, you can create your favorite playlist</h1>
    </v-row>
</template>

<script>
import axios from "../../node_modules/axios";
export default {
    data() {
        return {
            code: null,
            info: null,
            dialog: false
        };
    },
    mounted() {
        this.get_url();
        axios
            .get(
                "http://localhost:5000/get-token?code=" +
                    this.code.query["code"]
            )
            .then(
                response => (
                    (this.info = response["data"]),
                    (this.$store.state.jwt_token = response["data"]["jwt_token"]),
                    (this.$store.state.connected = true)
                )
            );
        console.log(this.$store.state.jwt_token)
        // let config = {
        //     headers: {
        //         jwt_token: this.$store.state.jwt_token
        //     }
        // };
        // axios
        //     .get("http://localhost:5000/get-user", config)
        //     .then(
        //         response => (
        //             (this.$store.state.user_photo =
        //                 response["data"][0]["user_photo"]),
        //             (this.$store.state.user_id =
        //                 response["data"][0]["user_id"]),
        //             console.log("ici:::" + response["data"])
        //         )
        //     );
    },
    methods: {
        get_url() {
            this.code = this.$route;
        }
    }
};
</script>

