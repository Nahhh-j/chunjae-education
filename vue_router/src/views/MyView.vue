<template>
  <div>
    <h1>This is My View</h1>

    <button @click="goHome">홈으로</button>
    <button @click="goAbout">어바웃으로</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function goHome() {
  router.push('/')
}

function goAbout() {
  router.push('/about')
}

</script>

<style lang="scss" scoped>

</style>