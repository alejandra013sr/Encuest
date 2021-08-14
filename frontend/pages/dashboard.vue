<template>
  <div class="container">
    <Card v-for="i in 5" :key="`n${i}`"/>
  </div>
</template>
<script>

import { mapGetters } from 'vuex'
  
export default {
  name: 'Dashboard',
  layout: 'dashboard',
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedUser'])
  }
}

</script>