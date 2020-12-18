<template>
  <div>
    <ChartPie v-if="info == 2" :centersTypes="centersTypes" />
    <ChartBar v-if="info == 2" :municipalities="municipalities"/>
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
      info: 0,
      centersTypes: {
        Plasma: 0,
        Sangre: 0,
        Ropa: 0,
        Comida: 0,
      },
      municipalities: {}
    };
  },

  created() {
    axios.get("http://localhost:5000/centers/by_type/").then((response) => {
      this.centersTypes.Plasma = response.data.Plasma;
      this.centersTypes.Sangre = response.data.Sangre;
      this.centersTypes.Ropa = response.data.Ropa;
      this.centersTypes.Comida = response.data.Comida;
      this.info ++;
    });
    axios.get("http://localhost:5000/centers/turns_by_municipality/").then((response)=>{
      this.municipalities = response.data;
      this.info++;
    });
  },
};
</script>
