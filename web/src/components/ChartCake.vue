<template>
  <v-card
    class="mx-auto"
    width="600"
    elevation="4"
    outlined
    style="border-radius: 8px;"
  >
    <v-card-title>
      <div>
        Total de turnos de tipo <em>{{ selectType }}</em> por municipio
      </div> 
    </v-card-title>
    <v-divider></v-divider>
    <v-card-text>
      <v-select
      v-model="selectType"
      :items="types"
      label="Tipo de centro de donación"
      @change="onChange($event)"
      ></v-select>
      <ve-pie :data="pieChartData"></ve-pie>
    </v-card-text>
  </v-card>
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
          console.log(this.pieChartData)
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