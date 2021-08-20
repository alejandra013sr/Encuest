<template>
  <div class="container">
    <Card v-for="image in images" :key="image.id">
      <template v-slot:header>
          <font-awesome-icon 
            icon="heart"
            color="#607d8b"
          />
        <h3>{{image.title}}</h3>
        {{image.id}}
        <button @click="deleteImage(image.id)">
          <font-awesome-icon 
            icon="trash-alt"
            color="#607d8b"
          />
        </button>
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