<template>
  <v-card>
    <v-toolbar
      class="primary"
      color="cyan"
      dark
      flat
      style="justify-content: center"
    >
      <v-toolbar-title>ayudAR</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items style="position: absolute">
        <v-btn depressed color="primary">
          <router-link to="/" style="color: white; text-decoration: none"
            >Home</router-link
          >
        </v-btn>
        <v-btn depressed color="primary">
          <router-link to="/Centers" style="color: white; text-decoration: none"
            >Centers</router-link
          >
        </v-btn>
      </v-toolbar-items>

      <!--       <template v-slot:extension>
        <v-tabs v-model="model" centered slider-color="yellow">
          <v-tab v-for="i in 3" :key="i" :href="`#tab-${i}`">
            Item {{ i }}
          </v-tab>
        </v-tabs>
      </template> -->
    </v-toolbar>
    <!--  <v-tabs-items v-model="model">
      <v-tab-item v-for="i in 3" :key="i" :value="`tab-${i}`">
        <v-card flat>
          <v-card-text v-text="text"></v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items> -->
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