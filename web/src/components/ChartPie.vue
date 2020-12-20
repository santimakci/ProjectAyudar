<template>
  <v-card
    class="mx-auto"
    width="600"
    elevation="4"
    outlined
    style="border-radius: 8px;"
  >
    <v-card-title>Cantidad de centros de ayuda por tipo</v-card-title>
    <v-divider></v-divider>
    <v-card-text>
      <ve-pie :data="pieChartData"></ve-pie>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  created() {},
  props: ["centersTypes"],
  data() {
    return {
      pieChartData: {
        columns: ["center_type", "amount"],
        rows: [
          { center_type: "Comida", amount: this.centersTypes.Comida },
          { center_type: "Ropa", amount: this.centersTypes.Ropa },
          { center_type: "Sangre", amount: this.centersTypes.Sangre },
          { center_type: "Plasma", amount: this.centersTypes.Plasma },
        ],
      },
    };
  },
  watch: {
    centersTypes: function (newVal, oldVal) {
      console.log("arreglo:", this.pieChartData.rows[0].center_type);
      console.log("dic:", this.pieChartData.rows);
      console.log(newVal, oldVal);
    },
  },
};
</script>