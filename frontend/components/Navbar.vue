<template>
  <div class="navbar">
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
    },
    user(){
      return this.$store.getters.loggedUser;
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