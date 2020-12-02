<template>
  <v-app>    
    <v-main>
      <NavInfo/>
      <Home/>
      <Footer/>
    </v-main>
  </v-app>
</template>

<script>
import Home from './components/Home';
import Footer from './components/Footer';
import NavInfo from './components/NavInfo';
export default {
  name: 'App',

  components: {
    Home,
    Footer,
    NavInfo
  },

  data: () => ({
    //
  }),
};
</script>
