<template>
  <main class="home__main">
    <div class="home__title">
      <span>Bienvenido a</span>
      <div class="home__name">
        <b>ENCUEST</b>
        <span>APP</span>
      </div>
    </div>
    <template v-if="!isAuthenticated">
      <NuxtLink to="/login" class="home__option">Login</NuxtLink>
      <NuxtLink to="/register" class="home__option">Register</NuxtLink>
    </template>

    <template v-else>
      <NuxtLink to="/dashboard" class="home__option">Dashboard</NuxtLink>
    </template>

  </main>
</template>

<script>
export default {
  layout: 'home',
  computed: {
    isAuthenticated(){
      return this.$store.state.auth.loggedIn;
    }
  },
  async created(){
    console.log(this);
    const res = await this.$axios.$get('profile/users/');
    console.log(res);
  }
}
</script>
