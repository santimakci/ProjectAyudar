<template>
  <v-row align="center" justify="space-around">
    <v-btn depressed color="primary">
      <router-link
        to="/cargarCentro"
        style="color: white; text-decoration: none"
        >Solicitar nuevo centro</router-link
      >
    </v-btn>
  </v-row>
</template>


<script>
import axios from "axios";

export default {
  name: "Centers",

  created() {
    axios
      .get("http://localhost:5000/centros")
      .then((response) => {
        /* debugger; */
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>