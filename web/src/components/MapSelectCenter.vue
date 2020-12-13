<template>
<div style="height: 500px; width: 100%">
 <l-map
      v-if="showMap"
      @click="setMarker"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 80%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
    <l-tile-layer :url="url" :attribution="attribution" />
      <l-marker
        :lat-lng="marker"
      >
       </l-marker>
    </l-map>
   </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LMarker  } from "vue2-leaflet";
import { Icon } from "leaflet";

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

export default {
  name: "MapSelectCenter",

  components: {
    LMap,
    LMarker,

  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    setMarker(e){
        this.marker = e.latlng;
        this.$emit('sendLat', {lat:this.marker.lat, lng:this.marker.lng});

    }
    },

  data (){
    return {
      zoom: 14,
      center: latLng(-34.920493, -57.949748),
      marker:[-34.920493, -57.949748],
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      currentZoom: 11.5,
      mapOptions: {
        zoomSnap: 0.5,
      },
      showMap: true,
    };
  },
  
};
</script>