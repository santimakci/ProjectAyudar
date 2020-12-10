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
              Nombre del centro: {{ cen.name }}<br />
              Dirección: {{ cen.adress }}<br />
              Horario: {{ cen.open_time }} - {{ cen.close_time }}<br />
              Teléfono: {{ cen.phone }}
            </p>
            <v-btn depressed color="primary" flat @click="dialog = true">
              Solicitar Turno
            </v-btn>
            <v-dialog v-model="dialog" persistent max-width="600px">
              <v-card>
                <AddTurn :center="cen" />
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="dialog = false">
                    Cerrar
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
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
import AddTurn from "@/components/AddTurn.vue";

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

export default {
  name: "MapCenter",
  components: {
    AddTurn,
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
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
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
  },
};
</script>