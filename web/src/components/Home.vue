<template>
  <v-container>
    <CarrouselIndex />
    <v-row>
      <Card/>
      <Card/>
      <Card/>
    </v-row>
  </v-container>
</template>

<script>
import CarrouselIndex from "./CarrouselIndex";
import Card from "./Card";
export default {
  name: "Home",
  components: {
    CarrouselIndex,
    Card
  },
};
</script>
