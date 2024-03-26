<template>
  <div>
    <h1 :class="myClass">Hello, {{ myClass }}</h1>
  </div>
</template>

<script setup>

const myText = 'Vue 3'
const myClass = ['bold', 'color', 'size']

</script>

<style lang="scss" scoped>
.bold {
  font-weight: bold;
}
.color {
  color: blueviolet;
}
.size {
  font-size: 5rem;
}
</style>