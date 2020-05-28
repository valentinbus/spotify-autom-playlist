<template>
    <div>{{ test }}</div>
</template>
<script>
import axios from "axios"
import checkToken from "../script/checkToken"

export default {
    data: () => ({
        test: null
    }),

    mounted() {
        let config = {
            headers: {
                jwt_token: this.$store.state.jwt_token
            }
        };
        axios
            .get("http://localhost:5000/check-token", config)
            .then(
                response => (
                    (this.test = response),
                    console.log("CHECK TOKEN:::" + response),
                    this.test = this.cathError(response)
                )
            );
    },
    methods: {
      cathError(response) {
        if(response['data']["error"]) {
          this.$store.state.connected = false
          return "Vous devez vous connectez avant"
        }
        else {
          return "ok"
        }
      }
    }

};
</script>