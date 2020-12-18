<template>
  <div>
    <ChartPie v-if="info == 3" :centersTypes="centersTypes" />
    <ChartBar v-if="info == 3" :municipalities="municipalities" />
    <ChartCake v-if="info == 3" :TotalTurnsByCenter="TotalTurnsByCenter" />
    <FlowerSpinner
      v-if="info != 3"
      :animation-duration="2500"
      :size="70"
      color="#ff1d5e"
    />
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
      .get("http://localhost:5000/centers/total_centers_by_type/")
      .then((response) => {
        this.TotalTurnsByCenter = response.data;
        console.log(response);
        this.info++;
      });

    axios.get("http://localhost:5000/centers/by_type/").then((response) => {
      this.centersTypes.Plasma = response.data.Plasma;
      this.centersTypes.Sangre = response.data.Sangre;
      this.centersTypes.Ropa = response.data.Ropa;
      this.centersTypes.Comida = response.data.Comida;
      this.info++;
    });
    axios
      .get("http://localhost:5000/centers/turns_by_municipality/")
      .then((response) => {
        this.municipalities = response.data;
        this.info++;
      });
  },
};
</script>
