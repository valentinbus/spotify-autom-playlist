<template>
    <div>
        <!-- <div>{{ this.$store.state.connected }}</div> -->
        <div>{{ this.$store.state.connected }}</div>
    </div>
</template>
<script>
import axios from "axios";

export default {
    data: () => ({
        test: null
    }),
};
</script>