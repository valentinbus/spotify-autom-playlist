<template>
    <v-row class="pa-4 text-center">
        <h1>Now, you can create your favorite playlist</h1>
        <h2>First synchronize you songs by clicking on "Synchronize".</h2>
        <h2>When it's done go on "Create Playlist" and select the playlist you want to create.</h2>
        <h2>You can resynchronize your songs by clicking on "Clear DB" then "Synchronize".</h2>
        </h2>
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
                "http://164.90.234.101:5000/#/get-token?code=" +
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
    },
    methods: {
        get_url() {
            this.code = this.$route;
        }
    }
};
</script>

