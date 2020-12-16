<template>
    <div>   
        <h1>total turnos sacados por municipio</h1>
        <ve-bar :data="chartData" height="1500px"></ve-bar>
    </div>
</template>

<script>
  export default {
    data () {
      return {
        chartData: {
          columns: ['date', 'Turnos sacados'],
          rows: [
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
            { 'date': 'CABA', 'Turnos sacados': 7123},            
            { 'date': 'San Nicolás', 'Turnos sacados': 123},
            { 'date': 'La plata', 'Turnos sacados': 1223},
            { 'date': 'Berazategui', 'Turnos sacados': 2123},
            { 'date': 'Quilmes', 'Turnos sacados': 4123},
            { 'date': 'Ensenada', 'Turnos sacados': 3123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
            { 'date': 'CABA', 'Turnos sacados': 7123},
          ]
        }
      }
    }
  }
</script>