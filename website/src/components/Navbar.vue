<template>
  <nav>
    <v-toolbar app>
      <v-toolbar-side-icon @click="drawer = !drawer" class="grey--text"></v-toolbar-side-icon>
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
      <v-layout column align-center>
        <v-flex class="mt-5">
          <v-avatar size="100">
            <img class="text-lg-center" :src="info[0]['user_photo']">
          </v-avatar>
          <p class="white--text subheading mt-1">{{ info[0]['user_id']  }}</p>
        </v-flex>
      </v-layout>
      <v-list>
        <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-tile-action>
            <v-icon class="white--text">{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title class="white--text">{{ link.text }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

  </nav>
</template>

<script>
import axios from '../../node_modules/axios'

export default {

  data() {
    return {
      user_name: null,
      user_photo: null,
      drawer: false,
      links: [
        { text: 'Dashboard', route: '/' },
        { text: 'My Projects', route: '/projects' },
        { text: 'Create Playlist', route: '/createplaylist' },
        { text: 'Login', route: '/connection' },
      ],
      snackbar: false
    }
  },
  mounted() {
      axios
          .get(
            "http://localhost:5000/get-user?user_id="+this.$session.get('user_id'),
            { user_id: 'valentinoiho'}
          )
          .then(
              response => (
                this.info = response['data'],
                console.log("ici:::"+response['data'])
              ),
          )
  },
}
</script>

<style>
</style>
