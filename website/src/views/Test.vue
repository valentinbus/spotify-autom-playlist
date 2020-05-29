<template>
    <div>
        <!-- <div>{{ this.$store.state.connected }}</div> -->
        <div>{{ checkToken }}</div>
    </div>
</template>
<script>
import axios from "axios";
import { mapGetters } from 'vuex';

export default {
    data: () => ({
        test: null
    }),
    computed: mapGetters([
      'checkToken'
    ])

};
</script>