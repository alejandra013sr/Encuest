<template>
  <div class="container">
    <Card v-for="image in images" :key="image.id">
      <template v-slot:header>
        <h3>{{image.title}}</h3>
      </template>
        <img class="image" :src="`http://localhost:8000${image.image}`">
        <p>{{image.description}}</p>

    </Card>
  </div>
</template>
<script>

import { mapGetters } from 'vuex'
  
export default {
  name: 'Dashboard',
  layout: 'dashboard',
  data(){
    return {
      images: []
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedUser'])
  },
  methods: {
    async getImages(){
      try {
        const res = await this.$axios.get('/imagenes/image');
        console.log(res);
        this.images = res.data;
        console.log(this.images);
      } catch (error) {
        console.log(error);
      }
    }
  },
  created(){
    this.getImages();
  }
}

</script>