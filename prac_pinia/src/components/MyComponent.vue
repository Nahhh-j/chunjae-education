<template>
  <div>
    <h2>my Component</h2>
    <input type="text" @input="onInput">
    <button @click="counterStore.increment">클릭!</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '/src/stores/counter'
import { useTextStore } from '../stores/text';

const counterStore = useCounterStore()
const textStore = useTextStore()

function onInput(e){
  // console.log(e.target.value)
  textStore.setText(e.target.value)
}

</script>

<style lang="scss" scoped>

</style>