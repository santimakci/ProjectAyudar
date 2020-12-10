<template>
  <v-carousel v-model="model"   
    cycle
    align="start"
    height="250"
    hide-delimiter-background
    show-arrows-on-hover>
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
      { type: "secondary", message: "Doná sangre" },
      { type: "accent", message: "Doná ropa" },
      { type: "info", message: "Doná comida" },
      { type: "warning", message: "Doná plasma" },
    ],
  }),
};
</script>