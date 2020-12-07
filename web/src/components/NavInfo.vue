<template>
  <v-card class="d-flex justify-center mb-6">
    <v-toolbar class="primary" color="cyan" dark flat>
      <v-toolbar-items
        class="margin-auto"
        style="margin: auto; margin-top: -5px"
      >
        <v-btn depressed color="primary">
          <router-link to="/" style="color: white; text-decoration: none"
            >Inicio</router-link
          >
        </v-btn>
        <v-btn depressed color="primary">
          <router-link to="/Centers" style="color: white; text-decoration: none"
            >Centros</router-link
          >
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