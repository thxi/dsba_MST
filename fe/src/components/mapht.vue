<template>
  <b-tabs content-class="mt-3">
    <b-tab
      :key="index"
      v-for="(map_name, index) in maps"
      :title="map_name"
      seamless
      >{{ `/maps/${map_name}${postfix}` }}
      <iframe :src="`/maps/${map_name}${postfix}`" seamless></iframe
    ></b-tab>

    <template slot="tabs">
      <b-button @click="markers()" variant="outline-primary"
        >{{ markers_prefix }} markers</b-button
      >
    </template>
  </b-tabs>
</template>

<script>

export default {
  name: 'mapht',
  data() {
    return {
      maps: ["boruvka"],
      enable_markers: false
    }
  },
  methods: {
    markers() {
      this.enable_markers = !this.enable_markers
    }
  },
  computed: {
    markers_prefix() {
      if (this.enable_markers) {
        return 'Disable'
      }
      return 'Enable'
    },
    postfix() {
      let s = "_map";
      if (this.enable_markers) {
        s += "_markers";
      }
      s += ".html";
      return s
    }
  }
}
</script>
<style scoped>
iframe {
  width: 100%;
  height: 100vh;
}
</style>
