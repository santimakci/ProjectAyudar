<template>
  <v-card class="d-flex justify-center mb-6">
    <v-toolbar class="primary" flat>
      <img class="mr-3" :src="require('../assets/logo.png')" height="25"/>
      <v-toolbar-items
        class="margin-auto"
        style="margin: auto; margin-top: -5px">
        <v-btn depressed color="primary" to="/" style="text-decoration: none"
            >Inicio
        </v-btn>
        <v-btn depressed color="primary" to="/centros" style="text-decoration: none"
            >Centros
        </v-btn>
        <v-btn depressed color="primary" to="/estadisticas" style="text-decoration: none"
            >Estadísticas
        </v-btn>
      </v-toolbar-items>   

    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      model: "tab-2",
      text: "Informacion ejemplo",
    };
  },
};
</script>

<style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Source Sans Pro");
  v-toolbar-title{
     font-family: Bold 700, 40px, "Source Sans Pro", sans-serif;
  }
</style>