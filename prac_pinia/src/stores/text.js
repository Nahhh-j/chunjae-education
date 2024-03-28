import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useTextStore = defineStore('text', () => {

  const text = ref('잘 들어갔니?')

  function setText(data){
    text.value = data
  }

  return { text, setText }
})
