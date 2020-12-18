<template>
  <div>
    <h1>Total de turnos de Tipo Plasma por Municipalidad</h1>
    <ve-pie :data="pieChartData"></ve-pie>
  </div>
</template>

<script>
export default {
  props: ["TotalTurnsByCenter"],
  created() {
    let rows = [];
    for (let dato of Object.keys(this.TotalTurnsByCenter)) {
      rows.push({
        Municipio: dato,
        amount: this.TotalTurnsByCenter[dato]["Total"],
      });
    }
    this.pieChartData.rows = rows;
  },

  data() {
    return {
      pieChartData: {
        columns: ["Municipio", "amount"],
        rows: [],
      },
    };
  },
};
</script>