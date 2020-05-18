<template>
<div>
</div>
</template>

<script>
import Header from './Header'
import Footer from './Footer'

export default {
  name: 'Presentation',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    Header,
    Footer
  }
}
</script>

<style>
@import "../css/body.css";
@import "../css/heading.css";
@import "../css/styles.css";
</style>
