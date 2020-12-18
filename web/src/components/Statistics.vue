<template>
  <div>
    <ChartPie v-if="info == true" :centersTypes="centersTypes" />
    <ChartBar />
  </div>
</template>


<script>
import ChartPie from "./ChartPie";
import ChartBar from "./ChartBar";
import axios from "axios";

export default {
  components: {
    ChartPie,
    ChartBar,
  },
  data() {
    return {
      info: false,
      centersTypes: {
        Plasma: 0,
        Sangre: 0,
        Ropa: 0,
        Comida: 0,
      },
    };
  },

  created() {
    axios.get("http://localhost:5000/centers/by_type/").then((response) => {
      this.centersTypes.Plasma = response.data.Plasma;
      this.centersTypes.Sangre = response.data.Sangre;
      this.centersTypes.Ropa = response.data.Ropa;
      this.centersTypes.Comida = response.data.Comida;
      this.info = true;
    });
  },
};
</script>
