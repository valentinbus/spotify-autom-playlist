<template>
  <v-container class="pa-4 text-center">
    <h1 class="grey--text m-12">Select the playlist you want to create</h1>
    <v-row class="fill-height" align="center" justify="center">
      <template v-for="(item, i) in info">
        <v-col
          :key="i"
          cols="12"
          md="4"
        >
          <v-hover>
            <v-card
              slot-scope="{ hover }"
              :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover }"
            >
              <v-img
                :src= "item.img"
                height="225px"
              >
                <v-card-title class="title white--text">
                  <v-row
                    class="fill-height flex-column"
                    justify="space-between"
                  >
                    <p class="mt-4 subheading text-left text-uppercase">{{ item.name }}</p>

                    <div>
                      <p class="ma-0 body-1 font-weight-bold font-italic text-left">
                        Based on your {{ item.name }} loved tracks 
                      </p>
                      <p class="caption font-weight-medium font-italic text-left">
                      </p>
                    </div>
                  </v-row>
                </v-card-title>
                <v-button icon 
                    class="{ 'show-btns': hover }"
                    color='transparent'
                    >
                        <v-icon
                        :class="{ 'show-btns': hover }"
                        color='transparent'>
                            add
                        </v-icon>
                    </v-button>
              </v-img>
            </v-card>
          </v-hover>
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>

<script>
import axios from '../../node_modules/axios'

  export default {
    data: () => ({
      name:'Presentation',
      icons: ['mdi-rewind', 'mdi-play', 'mdi-fast-forward'],
      info: null,
      url_img: [
        'https://images.unsplash.com/photo-1541256942802-7b29531f0df8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80',
        'https://images.unsplash.com/photo-1530982011887-3cc11cc85693?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2089&q=80',
        'https://images.unsplash.com/photo-1508898578281-774ac4893c0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',
        'https://images.unsplash.com/photo-1578792274110-c407602617da?ixlib=rb-1.2.1&auto=format&fit=crop&w=975&q=80',
        'https://images.unsplash.com/photo-1436262513933-a0b06755c784?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1651&q=80',
        'https://images.unsplash.com/photo-1559761132-5952db82b3e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80',
        'https://images.unsplash.com/photo-1528459584353-5297db1a9c01?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1975&q=80',
        'https://images.unsplash.com/photo-1435224654926-ecc9f7fa028c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80',
        'https://images.unsplash.com/photo-1527239441953-caffd968d952?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80',
        'https://images.unsplash.com/photo-1523730653024-1a0639ef3120?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=975&q=80'
      ],
      items: [
        {
          title: 'New Releases',
          text: "It's New Release Friday",
          subtext: 'Newly released songs. Updated daily.',
          img: 'http://lorempixel.com/output/nightlife-q-c-640-480-5.jpg',
        },
        {
          title: 'Rock',
          text: 'Greatest Rock Hits',
          subtext: 'Lose yourself in rock tunes.',
          img: 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80',
        },
        {
          title: 'Mellow Moods',
          text: 'Ambient Bass',
          subtext: 'Chill beats to mellow you out.',
          img: 'http://lorempixel.com/output/abstract-q-c-640-480-6.jpg',
        },
      ],
      transparent: 'rgba(255, 255, 255, 0)',
    }),
    mounted() {
    axios
    .get('http://localhost:5000/get-suggest-playlist')
    .then(response => 
      (
        this.info = this.add_url(response['data']['relevant_category'])
    ),
    )},
    methods: {
      add_url(response) {
        response[0].img = 'test'
        for(var i = 0; i<response.length; i++){
          response[i].img = this.url_img[i]
        }
        return response
    }
  }
}
</script>

<style scoped>
.v-card {
  transition: opacity .4s ease-in-out;
}

.v-card:not(.on-hover) {
  opacity: 0.6;
 }

.show-btns {
  color: rgba(255, 255, 255, 1) !important;
}
</style>