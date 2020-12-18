<template>
  <div>
    <h1>Total de turnos obtenidos, por municipio</h1>
    <ve-bar :data="chartData" height="3000px"></ve-bar>
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
        /*{ 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},            
            { 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},            
            { 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},            
            { 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},            
            { 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},*/
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