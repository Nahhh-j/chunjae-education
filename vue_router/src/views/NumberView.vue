<template>
  <div>
    <h1>
      {{ num }}
    </h1>
  </div>
</template>

<script setup>
import {useRoute} from 'vue-router'
const route = useRoute()

const num = route.params.num

</script>