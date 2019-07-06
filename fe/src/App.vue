<template>
  <div id="app">
    <mapht />
  </div>
</template>

<script>
import mapht from './components/mapht.vue'

export default {
  name: 'app',
  components: {
    mapht
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
