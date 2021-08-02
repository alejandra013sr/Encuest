<template>
  <main class="home__main">
    <div class="home__title">
      <span>Bienvenido a</span>
      <div class="home__name">
        <b>ENCUEST</b>
        <span>APP</span>
      </div>
    </div>
    <NuxtLink to="/login" class="home__option">Login</NuxtLink>
    <NuxtLink to="/register" class="home__option">Register</NuxtLink>
  </main>
</template>

<script>
export default {
  layout: 'home',
  async created(){
    const res = await this.$axios.$get('profile/users/');
    console.log(res);
  }
}
</script>
