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
      <div>
        <div
        v-if="load == false"
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
        <ve-pie v-if="load == true" :data="pieChartData"></ve-pie>
      </div>
      
    </v-card-text>
  </v-card>
</template>

<script>
import { FlowerSpinner } from "epic-spinners";
import axios from "axios";

export default {
  components: {
    FlowerSpinner,
  },
  props: ["TotalTurnsByCenter"],
  data() {
    return {
      load:true,
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
      this.load = false
      axios
        /*.get(
          "http://localhost:5000/centers/total_centers_by_type/?type=" + event
        )*/
        .get(
          "https://admin-grupo21.proyecto2020.linti.unlp.edu.ar/centers/total_centers_by_type/?type=" + event
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
          this.load = true
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