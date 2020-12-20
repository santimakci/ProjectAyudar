<template>
  <div>
    <div v-if="message.show">
      <v-alert v-if="message.status == 200" type="success">
        {{ message.text }}
      </v-alert>
      <v-alert v-else type="warning">
        {{ message.text }}
      </v-alert>
    </div>
    <div
    v-if="info == false"
    style="height: 70vh; display: flex; justify-content: center; align-items: center;"
    >
      <div 
      style="position: absolute; top: 50%; left: 50%; width: 60px; height: 60px; margin:-30px 0 0 -30px;"
      >
        <FlowerSpinner
        :animation-duration="2500"
        :size="70"
        color="#2BBBAD"
        />
      </div>
    </div>
    <v-container v-if="info == true">
      <v-row justify="space-between" class="pa-6 ma-2" align="end">
        <v-col>
          <h3 class="title">Centros de Donación</h3>
          <p class="text ma-0 grey--text">
            Buscá el más cercano, hace click en el marcador <br />y sacá turno
            para ir a donar!
          </p>
        </v-col>
        <v-btn
          depressed
          color="primary"
          to="/cargarCentro"
          style="color: white; text-decoration: none"
        >
          Solicitar nuevo centro
        </v-btn>
      </v-row>
      <MapCenters
        v-on:setMessage="showMessage"
        v-on:setShow="setShow"
        :centers="centers"
      />
    </v-container>
  </div>
</template>


<script>
import axios from "axios";
import MapCenters from "./MapCenters";
import { FlowerSpinner } from "epic-spinners";

export default {
  name: "Centers",

  components: {
    MapCenters,
    FlowerSpinner,
  },

  data() {
    return {
      info: false,
      centers: [],
      message: {
        text: "",
        status: "",
        show: false,
      },
    };
  },
  methods: {
    showMessage(args) {
      this.message.text = args.body;
      this.message.status = args.status;
      this.message.show = true;
    },
    setShow(status) {
      this.message.show = status;
    },
  },

  created() {
    axios
      /*.get("http://localhost:5000/centros") */
      .get("https://admin-grupo21.proyecto2020.linti.unlp.edu.ar/centros")
      .then((response) => {
        var totalPages = 1;
        if (response.data.count % response.data.limit != 0) {
          totalPages = response.data.count / response.data.limit + 1;
        } else {
          totalPages = response.data.count / response.data.limit;
        }
        for (var i = 1; i <= totalPages; i++) {
          /*let url = "http://localhost:5000/centros?page=" + i; */
          let url =
            "https://admin-grupo21.proyecto2020.linti.unlp.edu.ar/centros?page=" +
            i;
          axios.get(url).then((response) => {
            response.data.centros.forEach((center) => {
              if (center.status === "Aceptado") {
                this.centers.push(center);
              }
            });
            this.info=true
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>