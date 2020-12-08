<template>
  <v-container>
    <v-row align="center" justify="space-around">
      <v-btn depressed color="primary">
        <router-link
          to="/cargarCentro"
          style="color: white; text-decoration: none"
          >Solicitar nuevo centro</router-link
        >
      </v-btn>
    </v-row>
    <MapCenters :centers="centers" />
  </v-container>
</template>


<script>
import axios from "axios";
import MapCenters from "./MapCenters";

export default {
  name: "Centers",

  components: {
    MapCenters,
  },

  data() {
    return {
      centers: [],
    };
  },

  created() {
    axios
      .get("http://localhost:5000/centros")
      .then((response) => {
        var totalPages = 1;
        if (response.data.count % response.data.limit != 0) {
          totalPages = response.data.count / response.data.limit + 1;
        } else {
          totalPages = response.data.count / response.data.limit;
        }
        for (var i = 1; i <= totalPages; i++) {
          let url = "http://localhost:5000/centros?page=" + i;
          axios.get(url).then((response) => {
            response.data.centros.forEach((center) => {
              this.centers.push(center);
            });
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>