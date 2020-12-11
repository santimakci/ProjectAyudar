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
      v-bind:src="require('@/assets/' + img + '')"
    >
    </v-img>

    <v-card-title>{{title}}</v-card-title>
    
    <v-card-text>{{description}}</v-card-text>
    <v-chip
      class="primary--text ma-2" :to="link" style="text-decoration: none">{{name}}
    </v-chip>

  </v-card>
</template>

<script>
export default {
  data: () => ({
    
  }),
  name: "Card",
    props: {
    title: {
      type: String
    },
    img: {
      type: String
    },
    description: {
      type: String
    },
    link:{
      type: String
    },
    name:{
      type: String
    }
  },
};
</script>