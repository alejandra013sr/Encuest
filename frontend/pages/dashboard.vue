<template>
  <div>
    <span>{{ isAuthenticated }}</span>
    <div>{{ loggedUser }}</div>
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