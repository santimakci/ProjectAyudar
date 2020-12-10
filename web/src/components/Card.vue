<template>
 <v-card
    :loading="loading"
    class="mx-auto my-12 rounded-lg"
    max-width="374"
    
  >
    <template slot="progress">
      <v-progress-linear
        color="primary"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      src="../assets/map.png"
    >
     </v-img>

    <v-card-title>Encontrá tu centro de donación <br> más cercano</v-card-title>
    
    <v-card-text
    
    >
      <div>Sacá turno, y respetando los protocolos, acercá tus donaciones!</div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    
  }),
};
</script>