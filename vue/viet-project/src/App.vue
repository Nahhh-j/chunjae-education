<template>
  <div>
    <NavBarComponent @data-emitted="receiveDataFromNavBar" />
    <div class="d-flex">
      <AsideComponent />
      <MainComponent />
    </div>
    <div v-if="receivedData">
      Received Data: {{ receivedData }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import NavBarComponent from './components/NavBarComponent.vue';
import MainComponent from './components/MainComponent.vue';
import AsideComponent from './components/AsideComponent.vue';

const receivedData = ref('');

const receiveDataFromNavBar = (data) => {
  receivedData.value = data;
}
</script>

<style lang="scss" scoped>
</style>