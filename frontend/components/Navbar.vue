<template>
  <div>
    <h1>APP</h1>
    <span v-if="isAuthenticated">Hola</span>
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