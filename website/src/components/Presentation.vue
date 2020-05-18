<template>
<div class="page-section portfolio" id="portfolio">
                <!-- Portfolio Grid Items-->
    <div class="row justify-content-center">
        <!-- Portfolio Items-->
        <div class="col-md-12 col-lg-2 mb-5" v-for="item in items" :key="item.playlist">
            <div class="portfolio-item mx-auto" data-toggle="modal" data-target="#portfolioModal0">
                <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
                    <div class="portfolio-item-caption-content text-center text-white"><i class="fas fa-plus fa-3x"></i></div>
                </div>
                <img class="img-fluid" src="../assets/img/portfolio/cabin.png" alt="Log Cabin"/>
                <div class="text-block">
                    <h2 class="portfolio-modal-title text-dark mb-0">
                        {{ item.playlist }}
                    </h2>
                </div>
            </div>
            <h2 class="portfolio-modal-title text-dark mb-0">
                            {{ item.playlist }}
            </h2>
        </div>
    </div>
</div>
</template>

<script>
import axios from '../../node_modules/axios'
export default {
  name: 'Presentation',

  data () {
    return {
      info: null,
      items: [
        {
          playlist: 'rock'
        }
      ]
    }
  },
  mounted () {
    axios
      .get('http://localhost:5000/get-user')
      .then(response => (this.info = response))
  }
}
</script>

<style>
@import "../css/body.css";
@import "../css/heading.css";
@import "../css/styles.css";
</style>
