<template>
  <div class="home__wrapper principal">
    <header class="home__header">
      <div class="home__logo">
        <Logo width="40%" />
      </div>
      <div class="home__title">
        <span>Bienvenido a</span>
        <div class="home__name">
          <b>ENCUEST</b>
          <span>APP</span>
        </div>
      </div>
    </header>
    <main class="home__main">
      <NuxtLink to="/login" class="home__option">Login</NuxtLink>
      <NuxtLink to="/register" class="home__option">Register</NuxtLink>
    </main>
  </div>
</template>

<script>
export default {}
</script>
