<template>
  <v-footer padless>
    <v-row>
      <v-col class="py-4 primary--text" cols="8">
        <img :src="require('../assets/logoblack.png')"  height="50" style="margin-left: 40px;"/>
      </v-col>
      <v-col class="primary--text py-4" cols="4">
        <v-row>
          <v-col>
            <v-row>
              <span><strong>Contacto</strong></span>
            </v-row>
            <v-row>
              <span>ayudar@gba.gob.ar</span>
            </v-row>
          </v-col>
          <v-col>
            <v-row>
              <span><strong>Uso Interno</strong></span>
            </v-row>
            <v-row>
              <a class="primary--text" style="text-decoration: none" href="https://admin-grupo21.proyecto2020.linti.unlp.edu.ar">Administración</a>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
export default {
  data: () => ({}),
};
</script>
