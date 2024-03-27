<template>
  <div class="box">
    <h1>Main</h1>
    <div class="row">
      <ArticleComponent v-for="num in lst" :key="num" :articleNum="num" />
    </div>
  </div>
</template>

<script setup>
import ArticleComponent from './ArticleComponent.vue';
const lst = [1, 2, 3, 4, 5, 6];
</script>

<style lang="scss" scoped>
</style>