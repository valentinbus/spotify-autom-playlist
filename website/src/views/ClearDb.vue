<template>
    <div>
        <v-container class="pa-4 text-center" v-if="this.$store.state.connected==false">
            <h1>You have to be login</h1>
        </v-container>
        <div class="projects" v-if="this.$store.state.connected==true">
            <v-container class="my-5">
                <v-btn
                    color="primary"
                    text
                    :href="info"
                    @click="clear()"
                >Clear DB</v-btn>
            </v-container>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {};
    },
    methods: {
        clear() {
            axios({
                method: "delete",
                url: "http://164.90.234.101:5000/clear-db",
                headers: {
                    jwt_token: this.$store.state.jwt_token
                }
            })
                .then(function(response) {
                    //handle success
                    console.log(response.data);
                })
                .catch(function(response) {
                    //handle error
                    console.log(response.data);
                });
        }
    }
};
</script>
