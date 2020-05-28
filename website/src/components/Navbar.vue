<template>
    <nav>
        <v-toolbar app>
            <v-toolbar-side-icon @click="drawer = !drawer" class="grey--text"  v-on:click="loadData()"></v-toolbar-side-icon>
            <v-toolbar-title class="text-uppercase grey--text">
                <span>SPOTIFY</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>

            <!-- dropdown menu -->
            <v-menu offset-y>
                <v-btn flat slot="activator" color="grey">
                    <v-icon left>expand_more</v-icon>
                    <span>Menu</span>
                </v-btn>
                <v-list>
                    <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                        <v-list-tile-title>{{ link.text }}</v-list-tile-title>
                    </v-list-tile>
                </v-list>
            </v-menu>
        </v-toolbar>

        <v-navigation-drawer app v-model="drawer" class="primary" color="grey">
            <div v-if="this.$store.state.connected==true">
                <v-layout column align-center>
                    <v-flex class="mt-5">
                        <v-avatar size="100">
                            <img class="text-lg-center" :src="this.$store.state.user_photo" />
                        </v-avatar>
                        <p class="white--text subheading mt-1">{{ this.$store.state.user_id }}</p>
                    </v-flex>
                </v-layout>
                <v-list>
                    <v-list-tile
                        v-for="link in links_connected"
                        :key="link.text"
                        router
                        :to="link.route"
                    >
                        <div v-on:click="logOut(link.text)">
                            <v-list-tile-action>
                                <v-icon class="white--text">{{ link.icon }}</v-icon>
                            </v-list-tile-action>
                            <v-list-tile-content>
                                <v-list-tile-title class="white--text">{{ link.text }}</v-list-tile-title>
                            </v-list-tile-content>
                        </div>
                    </v-list-tile>
                </v-list>
            </div>
            <div v-if="this.$store.state.connected==false">
                <v-list>
                    <v-list-tile
                        v-for="link in links_disconnected"
                        :key="link.text"
                        router
                        :to="link.route"
                    >
                        <v-list-tile-action>
                            <v-icon class="white--text">{{ link.icon }}</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title class="white--text">{{ link.text }}</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </v-list>
            </div>
        </v-navigation-drawer>
    </nav>
</template>

<script>
import axios from "../../node_modules/axios";

export default {
    data() {
        return {
            user_name: null,
            user_photo: null,
            user_id: null,
            drawer: false,
            links_connected: [
                { text: "Dashboard", route: "/" },
                { text: "My Projects", route: "/projects" },
                { text: "Create Playlist", route: "/createplaylist" },
                { text: "Logout", route: "/connection" }
            ],
            links_disconnected: [
                { text: "Dashboard", route: "/" },
                { text: "Login", route: "/connection" }
            ],
            snackbar: false
        };
    },
    mounted() {},
    methods: {
        loadData() {

            let config = {
                headers: {
                    jwt_token: this.$store.state.jwt_token
                }
            };
            this.connected = this.$store.state.connected;
            console.log("connected:::" + this.connected);

            axios
                .get("http://localhost:5000/get-user", config)
                .then(
                    response => (
                        (this.info = response["data"]),
                        (this.$store.state.user_photo = response["data"][0]["user_photo"]),
                        (this.$store.state.user_id = response["data"][0]["user_id"]),
                        console.log("ici:::" + response["data"])
                    )
                );
        },
        logOut(button) {
            if (button == "Logout") {
                this.$store.state.connected = false;
                console.log(
                    "logout connected state:::" + this.$store.state.connected
                );
            }
        }
    }
};
</script>

<style>
</style>
