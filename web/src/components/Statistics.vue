<template>
  <v-img src="../assets/construccion.png">
    <template v-slot:placeholder>
      <v-row class="fill-height ma-0" align="center" justify="center">
        <v-progress-circular
          indeterminate
          color="blue darken-2"
        ></v-progress-circular>
      </v-row>
    </template>
  </v-img>
</template>


<script>
export default {
  data: () => ({}),
};
</script>
