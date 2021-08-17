<template>
  <div class="card__wrapper">
    <div class="card">
      <header class="card__header">
        <slot name="header"></slot>
      </header>
      <main class="card__main">
        <slot></slot>
      </main>
      <footer class="card__footer">
        <slot name="footer"></slot>
      </footer>
    </div>
  </div>
</template>
<script>
  
export default {
  name: 'Card'
}

</script>