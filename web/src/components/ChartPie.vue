<template>
  <div>
    <h1>Cantidad de centros de ayuda por tipo</h1>
    <ve-pie :data="pieChartData"></ve-pie>
  </div>
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
          { center_type: "Sangre", amount: this.centersTypes.Sangre },
          { center_type: "Plasma", amount: this.centersTypes.Plasma },
          { center_type: "Comida", amount: this.centersTypes.Comida },
          { center_type: "Ropa", amount: this.centersTypes.Ropa },
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