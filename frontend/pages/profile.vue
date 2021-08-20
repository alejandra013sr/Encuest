<template>
  <Card>
    <b>Nombre:</b>
    <span>{{ user.name }}</span>

    <b>Email:</b>
    <span>{{ user.email }}</span>
  </Card>
</template>
<script>
  
export default {
  name: 'Profile',
  layout: 'dashboard',
  computed: {
    user(){
      return this.$store.getters.loggedUser;
    }
  }
}

</script>