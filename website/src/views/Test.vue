<template>
  <v-row justify="center">
    <v-btn
      color="primary"
      text
      :href="info"
    >
      Login
    </v-btn>
  </v-row>
</template>

<script>
import axios from '../../node_modules/axios'
  export default {
    data () {
      return {
        info: null,
        dialog: false,
      }
    },
    mounted() {
      console.log("je suis ici")
      axios
          .get(
            "http://localhost:5000/authent",
            {
                headers: {
                     "Access-Control-Allow-Origin": "*",
                }
            }
          )
          .then(
              response =>
                  (this.info =(
                      response['data']
                  ),
                  console.log("ICI:::"+response['data'])
                  )
          );
  },
  }
</script>

