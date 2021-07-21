<template>
	<div class="home" :class="{ 'principal' : !authMode }">
		<header class="home__header">
        <Logo :class="{ 'logo--auth' : authMode }" />
    </header>
		<Nuxt />
	</div>
</template>
<script>
export default {
	name: 'HomeLayout',
  data(){
    return {
      authMode: false
    }
  },
  watch: {
    $route(to){
      if (to.name !== 'index') {
        this.authMode = true;
      } else {
        this.authMode = false;
      }
    }
  },
  created(){
    this.authMode = this.$nuxt.$route.name !== 'index' ? true : false;
  },
}
</script>