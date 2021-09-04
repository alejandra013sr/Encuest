<template>
  <div class="dashboard">
    <notifications position="bottom right"/>
    <header>
      <Navbar />
    </header>
    <main>
      <Nuxt />
    </main>
    <footer>
      <NavbarMenu2 />
    </footer>
  </div>
</template>
<script>
  
export default {
  name: 'DashboardLayout',
  middleware: 'auth'
}

</script>