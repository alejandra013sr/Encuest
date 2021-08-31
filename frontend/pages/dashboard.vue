<template>
  <div class="container">
    <ImagePost 
      v-for="image in images" 
      :key="image.id" 
      :image="image"
    />
  </div>
</template>
<script>

import { mapGetters } from 'vuex'
  
export default {
  name: 'Dashboard',
  layout: 'dashboard',
  data(){
    return {

    }
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedUser']),
    images(){
      return this.$store.state.images
    }
  },
  methods: {
    deleteImage(id){
      this.$store.dispatch('deleteImage', id);
    }
  },
  created(){
    this.$store.dispatch('images');
  }
}

</script>