<template>
  <div id="app">
    <Nodes />
  </div>
</template>
<script>
import Nodes from './components/Nodes.vue'
export default {
  name: 'app',/*
  methods: {
  test: function() {
  alert('salut')
  }
  },*/
  components: {
    Nodes
  }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
