<template>
  <v-carousel v-model="model"   
    cycle
    align="start"
    height="250"
    hide-delimiter-background
    show-arrows-on-hover>
    <v-carousel-item v-for="color in colors" 
    :key="color"
    :src="require('@/assets/' + color.img + '')">
      <span class="font-weight-black text-h2 text-center">{{ color.message }}</span>
    </v-carousel-item>
  </v-carousel>
</template>


<script>
export default {
  data: () => ({
    model: 0,
    colors: [
      { img: "sangre.jpg", message: "Doná sangre" },
      { img: "ropa.jpg", message: "Doná ropa" },
      { img: "comida.jpg", message: "Doná comida" },
      { img: "plasma.jpg", message: "Doná plasma" },
    ],
  }),
};
</script>