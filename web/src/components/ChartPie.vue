<template>
  <div>
    <h1>Cantidad de centros de ayuda por tipo</h1>
    <ve-pie :data="pieChartData"></ve-pie>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        pieChartData: {
          columns: ['center_type', 'amount'],
          rows: [
            { 'center_type': 'Sangre', 'amount': 15},
            { 'center_type': 'Plasma', 'amount': 20},
            { 'center_type': 'Comida', 'amount': 18},
            { 'center_type': 'Ropa', 'amount': 10},
          ]
        }
      }      
    }
  }
</script>