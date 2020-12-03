<template>
  <v-carousel v-model="model">
    <v-carousel-item v-for="color in colors" :key="color">
      <v-sheet :color="color.type" height="100%" tile>
        <v-row class="fill-height" align="center" justify="center">
          <div class="display-3">{{ color.message }}</div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>


<script>
export default {
  data: () => ({
    model: 0,
    colors: [
      { type: "primary", message: "Alguna boludez pa centro" },
      { type: "primary", message: "Alguna boludez pa turnos" },
      { type: "primary", message: "?????" },
    ],
  }),
};
</script>