<template>
  <v-app>
    <v-main>
      <NavInfo />
      <router-view />
      <Footer />
    </v-main>
  </v-app>
</template>

<script>
import Footer from "./components/Footer";
import NavInfo from "./components/NavInfo";

export default {
  name: "App",

  components: {
    Footer,
    NavInfo,
  },

  data: () => ({
    //
  }),
};
</script>
