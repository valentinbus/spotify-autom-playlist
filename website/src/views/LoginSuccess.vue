<template>
<v-row class="pa-4 text-center">
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
                  this.$session.start(),
                  this.$session.set("jwt_token", response['data']['jwt_token'])
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

