<template>
  <div>
    <h1>Total de turnos de Tipo {{ selectType }} por Municipalidad</h1>
    <v-select
      v-model="selectType"
      :items="types"
      label="Tipo de centro *"
      @input="$v.center.center_type.$touch()"
      @blur="$v.center.center_type.$touch()"
      @change="onChange($event)"
    ></v-select>
    <ve-pie :data="pieChartData"></ve-pie>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: ["TotalTurnsByCenter"],
  data() {
    return {
      selectType: "Plasma",
      types: ["Sangre", "Plasma", "Comida", "Ropa"],
      pieChartData: {
        columns: ["Municipio", "amount"],
        rows: [],
      },
    };
  },

  methods: {
    onChange(event) {
      axios
        .get(
          "http://localhost:5000/centers/total_centers_by_type/?type=" + event
        )
        .then((response) => {
          let rows = [];
          for (let dato of Object.keys(response.data)) {
            rows.push({
              Municipio: dato,
              amount: response.data[dato]["Total"],
            });
          }
          this.pieChartData.rows = rows;
        });
    },
  },
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
};
</script>