<template>
  <div>
    <h1>my App</h1>
    <div>text : {{ textStore.text }}</div>
    <MyComponent />
  </div>
</template>

<script setup>
import MyComponent from './components/MyComponent.vue';
import { useCounterStore } from './stores/counter'
import { useTextStore } from './stores/text'


const counterStore = useCounterStore()
const textStore = useTextStore()

</script>

<style lang="scss" scoped>

</style>