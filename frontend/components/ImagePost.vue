<template>
  <Card>
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
</template>
<script>
  
export default {
  name: 'ImagePost',
  props: {
    image: {
      type: Object,
      required: true
    }
  },
  async created(){
    const res = await this.$axios.$put('/imagenes/image/detail/', {
      id: this.image.id
    });
  }
}

</script>