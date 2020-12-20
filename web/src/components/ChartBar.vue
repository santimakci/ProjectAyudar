<template>
  <div>
    <div 
    style="margin:30px; 
    height:400px; 
    border: thin solid rgba(0,0,0,.12);
    border-radius:8px; 
    overflow:auto; 
    box-shadow: 0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12);" 
    >
      <h2 
      style="padding: 16px;
      font-size: 1.25rem;
      font-weight: 500;
      letter-spacing: .0125em;
      line-height: 2rem;
      word-break: break-all;">
        Total de turnos obtenidos por municipio
      </h2>
      <v-divider></v-divider>
      <ve-bar :data="chartData" height="3000px"></ve-bar>
    </div>
  </div>
</template>

<script>
export default {
  props: ["municipalities"],
  data() {
    return {
      chartData: {
        columns: ["Municipio", "Turnos sacados"],
        rows: [],
      },
    };
  },
  created() {
    let rows = [];
    for (let muni of Object.keys(this.municipalities)) {
      rows.push({
        Municipio: muni,
        "Turnos sacados": this.municipalities[muni]["turnos"],
      });
    }
    this.chartData.rows = rows;
  },
};
</script>