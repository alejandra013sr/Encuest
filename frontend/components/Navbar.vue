<template>
  <div class="navbar">
    <h1>Hola User!!</h1>
    <div v-if="isAuthenticated">
      <button @click="logout">Logout</button>
    </div>
  </div>
</template>
<script>
  
export default {
  name: 'Navbar',
  computed: {
    isAuthenticated(){
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    async logout(){
      this.$auth.logout();
    }
  },
  mounted(){
    console.log(this.$auth);
  }
}

</script>