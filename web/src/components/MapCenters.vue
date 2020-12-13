<template>
  <div style="height: 500px; width: 100%">
    <l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 80%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-marker
        v-for="cen in centers"
        :key="cen.name"
        :lat-lng="[cen.lat, cen.lng]"
      >
        <l-popup>
          <div>
            <p>
              <strong>Nombre del centro:</strong> {{ cen.name }}<br />
              <strong>Dirección:</strong> {{ cen.adress }}<br />
              <strong>Horario:</strong> {{ cen.open_time }} - {{ cen.close_time
              }}<br />
              <strong>Teléfono:</strong> {{ cen.phone }} <br />
              <strong>Tipo:</strong> {{ cen.type }}
            </p>
            <Dialog
              v-on:superMSJ="upResponse"
              v-on:showOff="show"
              :center="cen"
            />
          </div>
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";
import { Icon } from "leaflet";
import Dialog from "@/components/Dialog";

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

export default {
  name: "MapCenter",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    Dialog,
  },
  data() {
    return {
      zoom: 14,
      center: latLng(-34.920493, -57.949748),
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      currentZoom: 11.5,
      mapOptions: {
        zoomSnap: 0.5,
      },
      showMap: true,

      dialog: false,
    };
  },
  props: ["centers"],
  methods: {
    show(status) {
      this.$emit("setShow", status);
    },
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    upResponse(args) {
      this.$emit("setMessage", args);
    },
  },
};
</script>