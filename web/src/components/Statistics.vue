<template>
  <div>
    <v-row>
      <ChartPie v-if="info == 3" :centersTypes="centersTypes" />
      <ChartCake v-if="info == 3" :TotalTurnsByCenter="TotalTurnsByCenter" />
    </v-row>
    <ChartBar v-if="info == 3" :municipalities="municipalities" />
    <div
    v-if="info != 3"
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
  </div>
</template>


<script>
import { FlowerSpinner } from "epic-spinners";
import ChartPie from "./ChartPie";
import ChartBar from "./ChartBar";
import ChartCake from "./ChartCake";
import axios from "axios";

export default {
  components: {
    ChartPie,
    ChartBar,
    ChartCake,
    FlowerSpinner,
  },
  data() {
    return {
      info: 0,
      centersTypes: {
        Plasma: 0,
        Sangre: 0,
        Ropa: 0,
        Comida: 0,
      },
      municipalities: {},
      TotalTurnsByCenter: {},
    };
  },

  created() {
    axios
      /*.get("http://localhost:5000/centers/total_centers_by_type/")*/
      .get("http://admin-grupo21.proyecto2020.linti.unlp.edu.ar/centers/total_centers_by_type/")
      .then((response) => {
        this.TotalTurnsByCenter = response.data;
        console.log(response);
        this.info++;
      });

    axios
    /*.get("http://localhost:5000/centers/by_type/")*/
    .get("http://admin-grupo21.proyecto2020.linti.unlp.edu.ar/centers/by_type/")
    .then((response) => {
      this.centersTypes.Plasma = response.data.Plasma;
      this.centersTypes.Sangre = response.data.Sangre;
      this.centersTypes.Ropa = response.data.Ropa;
      this.centersTypes.Comida = response.data.Comida;
      this.info++;
    });
    axios
      /*.get("http://localhost:5000/centers/turns_by_municipality/")*/
      .get("http://admin-grupo21.proyecto2020.linti.unlp.edu.ar/centers/turns_by_municipality/")
      .then((response) => {
        this.municipalities = response.data;
        this.info++;
      });
  },
};
</script>
