<template>
  <div>
    <v-card class="d-flex justify-center mb-6" v-if="!$vuetify.breakpoint.xs">
      <v-toolbar class="primary" flat>
        <img class="mr-3" :src="require('../assets/logo.png')" height="25"/>
        <v-toolbar-items
        class="margin-auto"
        style="margin: auto; margin-top: -5px">
          <v-btn depressed color="primary" to="/" style="text-decoration: none"
            >Inicio
          </v-btn>
          <v-btn depressed color="primary" to="/centros" style="text-decoration: none"
            >Centros
          </v-btn>
          <v-btn depressed color="primary" to="/estadisticas" style="text-decoration: none"
            >Estadísticas
          </v-btn>
        </v-toolbar-items>   
      </v-toolbar>
    </v-card>  
    <!-- mobile -->
      <v-app-bar
      color="primary"
      dark
      v-if="$vuetify.breakpoint.xs"
      >
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
        <v-toolbar-title><img class="mr-3" :src="require('../assets/logo.png')" height="25"/></v-toolbar-title>
      </v-app-bar>
      <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
      >
        <v-list
        nav
        dense
        >
          <v-list-item-group
          v-model="group"
          active-class="primary--text text--accent-4"
          >
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-home</v-icon>
              </v-list-item-icon>
              <router-link to="/" style="text-decoration: none" class="black--text text--accent-4">
                Inicio
              </router-link>
            </v-list-item>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-office-building</v-icon>
              </v-list-item-icon>
              <router-link class="black--text text--accent-4" to="/centros" style="text-decoration: none">
                Centros
              </router-link>
            </v-list-item>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-chart-bar</v-icon>
              </v-list-item-icon>
              <router-link class="black--text text--accent-4" to="/estadisticas" style="text-decoration: none">
                Estadísticas
              </router-link>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      model: "tab-2",
      drawer: false,
      group: null,
    };
  },
  watch: {
    group () {
      this.drawer = false
    },
  },
}
</script>

<style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Source Sans Pro");
  v-toolbar-title{
     font-family: Bold 700, 40px, "Source Sans Pro", sans-serif;
  }
</style>