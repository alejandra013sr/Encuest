<template>
  <div class="container">
    <Card>
      <template v-slot:header>
        <h3>Agregar imagen</h3>
      </template>
      <template v-slot:default>
        <AddImage />
      </template>
    </Card>
  </div>
</template>
<script>
  
export default {
  name: 'Profile',
  layout: 'dashboard'
}

</script>