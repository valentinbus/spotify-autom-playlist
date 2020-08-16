<template>
    <div>
        <v-container class="pa-4 text-center" v-if="this.$store.state.connected==false">
            <h1>You have to be login</h1>
        </v-container>
        <v-container class="pa-4 text-center" v-if="this.$store.state.connected==true">
            <h1 class="grey--text m-12">Select the playlist you want to create</h1>
            <v-row class="fill-height" align="center" justify="center">
                <template v-for="(item, i) in info">
                    {{ test }}
                    <v-col :key="i" cols="12" md="4">
                        <v-hover>
                            <v-card
                                slot-scope="{ hover }"
                                :elevation="hover ? 12 : 2"
                                :class="{ 'on-hover': hover }"
                            >
                                <v-img
                                    @click="choose(item.id), playlistName(item.name)"
                                    @click.stop="dialog = true"
                                    :src="item.img"
                                    height="225px"
                                >
                                    <v-card-title class="title white--text">
                                        <v-row
                                            class="fill-height flex-column"
                                            justify="space-between"
                                        >
                                            <p
                                                class="mt-4 subheading text-left text-uppercase"
                                            >{{ item.name }}</p>
                                            <div>
                                                <p
                                                    class="ma-0 body-1 font-weight-bold font-italic text-left"
                                                >Based on your {{ item.name }} loved tracks</p>
                                                <p
                                                    class="caption font-weight-medium font-italic text-left"
                                                ></p>
                                            </div>
                                        </v-row>
                                    </v-card-title>
                                    <v-btn
                                        icon
                                        class="{ 'show-btns': hover }"
                                        color="transparent"
                                        v-bind:style="{cursor: pointer}"
                                    >
                                        <v-icon
                                            :class="{ 'show-btns': hover }"
                                            color="transparent"
                                        >add</v-icon>
                                    </v-btn>
                                </v-img>
                            </v-card>
                        </v-hover>
                    </v-col>
                </template>
            </v-row>
            <div class="dialog">
                <v-row justify="center">
                    <v-dialog content-class="v-dialog" v-model="dialog" max-width="290">
                        <div class="dialog">
                            <v-card-title class="headline">Warning</v-card-title>

                            <v-card-text>Are you sure to want to create {{ playlist_name }} playlist ?</v-card-text>

                            <v-card-actions>
                                <v-spacer></v-spacer>

                                <v-btn color="primary" text @click="dialog = false">Disagree</v-btn>

                                <v-btn
                                    color="primary"
                                    text
                                    @click="createPlaylist(chosen_playlist), dialog=false"
                                >Agree</v-btn>
                            </v-card-actions>
                        </div>
                    </v-dialog>
                </v-row>
            </div>
        </v-container>
    </div>
</template>

<script>
import axios from "../../node_modules/axios";

export default {
    data: () => ({
        chosen_playlist: null,
        playlist_name: null,
        popup: false,
        test: null,
        name: "CreatePlaylist",
        icons: ["mdi-rewind", "mdi-play", "mdi-fast-forward"],
        info: null,
        dialog: false,
        url_img: [
            "https://images.unsplash.com/photo-1578792274110-c407602617da?ixlib=rb-1.2.1&auto=format&fit=crop&w=975&q=80",
            "https://images.unsplash.com/photo-1436262513933-a0b06755c784?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1651&q=80",
            "https://images.unsplash.com/photo-1559761132-5952db82b3e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80",
            "https://images.unsplash.com/photo-1487088678257-3a541e6e3922?ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80",
            "https://images.unsplash.com/photo-1541778956252-6c31bbd0ff64?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2089&q=80",
            "https://images.unsplash.com/photo-1541256942802-7b29531f0df8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80",
            "https://images.unsplash.com/photo-1508898578281-774ac4893c0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80",
            "https://images.unsplash.com/photo-1528459584353-5297db1a9c01?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1975&q=80",
            "https://images.unsplash.com/photo-1527239441953-caffd968d952?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80",
            "https://images.unsplash.com/photo-1544306094-e2dcf9479da3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80"
        ],
        transparent: "rgba(255, 255, 255, 0)"
    }),

    mounted() {
        let config = {
            headers: {
                jwt_token: this.$store.state.jwt_token
            }
        };
        axios
            .get("http://164.90.234.101:5000/#/get-suggest-playlist", config)
            .then(
                response =>
                    (this.info = this.add_url(
                        response["data"]["relevant_category"]
                    ))
            );
    },
    methods: {
        add_url(response) {
            for (var i = 0; i < response.length; i++) {
                response[i].img = this.url_img[i];
            }
            return response;
        },
        choose(chosen_playlist) {
            console.log(chosen_playlist);
            this.chosen_playlist = chosen_playlist;
        },
        playlistName(playlist_name) {
            this.playlist_name = playlist_name
        },
        createPlaylist(chosen_playlist) {
            let config = {
                headers: {
                    jwt_token: this.$store.state.jwt_token
                }
            };
            var bodyFormData = new FormData();
            bodyFormData.set("category_id", chosen_playlist);

            axios({
                method: "post",
                url: "http://164.90.234.101:5000/#/create-playlist",
                data: bodyFormData,
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

<style scoped>
.v-card {
    transition: opacity 0.4s ease-in-out;
}

.v-card:not(.on-hover) {
    opacity: 0.6;
}

.show-btns {
    color: rgba(255, 255, 255, 1) !important;
}

.v-icon {
    cursor: pointer;
}

.dialog {
    background: white;
}

.v-dialog {
    background: white;
}

.v-dialog__content {
    box-shadow: None;
}
</style>