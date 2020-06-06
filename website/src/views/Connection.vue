<template>
    <div>
        <h1
            v-if="this.$store.state.message_connection != null"
        >{{ this.$store.state.message_connection }}</h1>
        <v-container class="my-5">
            <v-btn class="ml-5" color="primary" text :href="info" v-on:click="logIn()">Login</v-btn>
        </v-container>
    </div>
</template>

<script>
import axios from "../../node_modules/axios";
export default {
    data() {
        return {
            info: null,
            dialog: false
        };
    },
    methods: {
        logIn() {
            this.$store.state.connected = true;
        }
    },
    mounted() {
        console.log((this.$store.state.connected = false));
        axios
            .get("http://localhost:5000/authent", {
                headers: {
                    "Access-Control-Allow-Origin": "*"
                }
            })
            .then(
                response => (
                    (this.info = response["data"]),
                    console.log("ICI:::" + response["data"])
                )
            );
    }
};
</script>

