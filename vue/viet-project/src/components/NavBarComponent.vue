<template>
  <div class="box">
    <h1>NavBar</h1>
    <button @click="emitData">Emit Data</button>
  </div>
</template>

<script setup>
import { defineEmits } from 'vue';

const emitData = () => {
  emit('data-emitted', 'Data from NavBar');
}

defineEmits(['data-emitted']);
</script>

<style lang="scss" scoped>
</style>