<template>
  <b-tabs content-class="mt-3" v-model="tabIndex">
    <b-tab
      :key="index"
      v-for="(map_name, index) in maps"
      :title="map_name"
      seamless
      >{{ map_name }}
      <iframe :src="`/maps/${map_name}${postfix}`" seamless></iframe
    ></b-tab>

    <template slot="tabs" v-if="tabIndex != 3">
      <b-button @click="markers()" variant="outline-primary"
        >{{ markers_prefix }} markers</b-button
      >
    </template>
    <template slot="tabs" v-if="tabIndex != 3">
      <b-button @click="cities()" variant="outline-primary"
        >Use {{ cities_prefix }} cities</b-button
      >
    </template>
    <b-tab title="Yandex map">
      <yMap />
    </b-tab>
  </b-tabs>
</template>

<script>
import yMap from '@/components/yMap.vue'

export default {
  name: 'mapht',
  components: {
    yMap
  },
  data() {
    return {
      maps: ["boruvka", "prim", "kruskal"],
      enable_markers: false,
      enable_cities: false,
      tabIndex: 0
    }
  },
  methods: {
    markers() {
      this.enable_markers = !this.enable_markers
    },
    cities() {
      this.enable_cities = !this.enable_cities
    }
  },
  computed: {
    cities_prefix() {
      if (this.enable_cities) {
        return 'Large'
      }
      return 'Small'
    },
    markers_prefix() {
      if (this.enable_markers) {
        return 'Disable'
      }
      return 'Enable'
    },
    postfix() {
      let s = "_map"
      if (this.enable_markers) {
        s += "_markers"
      }
      if (this.enable_cities) {
        s += "_v1"
      } else {
        s += "_v2"
      }
      s += ".html"
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
