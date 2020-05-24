<template>
<v-row class="pa-4 text-center">
  {{ info }}
    <h1>Now, you can create your favorite playlist</h1>
  </v-row>
</template>

<script>
import axios from '../../node_modules/axios'
  export default {
    data () {
      return {
        code: null,
        info: null,
        dialog: false,
      }
    },
    mounted() {
      this.get_url()
      axios
          .get(
            "http://localhost:5000/get-token?code="+this.code.query['code'],
          )
          .then(
              response =>
                  (this.info =(
                      response['data']
                  ),
                  console.log("ICI:::"+response['data'][0]['user_id']),
                  this.$session.start(),
                  this.$session.set("user_id", response['data'][0]['user_id']),
                  this.$session.set("baerer_token", response['data'][0]['baerer_token']),
                  console.log(this.$session.get('user_id'))
              ),
          );
    },
    methods: {
      get_url(){
        this.code = this.$route
      } 
    }
  }
</script>

