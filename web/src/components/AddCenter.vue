<template>
  <div>
    <v-card class="pa-md-4 mx-lg-auto" style="width: 60%; margin: auto">
      <form @submit.prevent="createCenter" id="new-center">
        <v-card v-for="e in errors" :key="e.id">
          <v-alert color="red" dense dismissible elevation="17" outlined text>
            {{ e.error }}</v-alert
          >
        </v-card>

        <v-text-field
          v-model="center.name"
          id="name"
          :error-messages="nameErrors"
          label="Nombre del centro"
          required
        ></v-text-field>
        <v-text-field
          v-model="center.address"
          :error-messages="nameErrors"
          label="Dirección"
        ></v-text-field>
        <v-text-field
          v-model="center.phone"
          :error-messages="nameErrors"
          label="Teléfono"
          type="number"
        ></v-text-field>
        <v-text-field
          v-model="center.email"
          :error-messages="emailErrors"
          label="E-mail"
          type="email"
          @input="$v.email.$touch()"
        ></v-text-field>

        <v-row justify="center">
          <v-col md="6">
            <v-menu
              ref="menu"
              v-model="menu2"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="center.open_time"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="center.open_time"
                  label="Hora de apertura"
                  prepend-icon="mdi-clock-time-four-outline"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-time-picker
                v-model="time"
                full-width
                @click:minute="$refs.menu.save(time)"
              ></v-time-picker>
            </v-menu>
          </v-col>

          <v-col md="6">
            <v-menu
              ref="menu2"
              v-model="menu"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="center.close_time"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="center.close_time"
                  label="Hora de cierre"
                  prepend-icon="mdi-clock-time-four-outline"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-time-picker
                v-model="timeClose"
                full-width
                @click:minute="$refs.menu2.save(timeClose)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>
        <v-select
          v-model="center.center_type"
          :items="center_type"
          :error-messages="selectErrors"
          label="Tipo de centro"
          @change="$v.select.$touch()"
        ></v-select>
        <v-select
          v-model="center.municipality"
          :items="municipalitys"
          :error-messages="selectErrors"
          label="Municipalidad"
          @change="$v.select.$touch()"
        ></v-select>
        <v-text-field
          v-model="center.web"
          :error-messages="nameErrors"
          label="Página web"
        ></v-text-field>
        <vue-recaptcha
          sitekey="6LfzZf0ZAAAAALQeKk_wfuct6zzTj9TlRiKzKaEV"
        ></vue-recaptcha>
        <v-row justify="center">
          <v-btn type="submit" form="new-center" class="primary">
            Enviar centro
          </v-btn>
        </v-row>
      </form>
    </v-card>
    <br />
  </div>
</template>

<script>
import axios from "axios";
import VueRecaptcha from "vue-recaptcha";

export default {
  name: "AddCenter",
  components: { VueRecaptcha },

  data() {
    return {
      errors: [],
      center_type: ["Alimentos", "Sangre", "Ropa", "Plasma"],
      municipalitys: [],
      center: {
        name: "",
        address: "",
        phone: "",
        open_time: "",
        close_time: "",
        center_type: "",
        municipality: "",
        lat: "",
        lng: "",
        email: "",
        web: "",
      },
    };
  },
  methods: {
    checkForm() {
      if (
        this.name &&
        this.address &&
        this.phone &&
        this.email &&
        this.open_time &&
        this.close_time &&
        this.municipality &&
        this.center_type
      ) {
        return true;
      }
      this.errors = [];
      if (!this.name) {
        this.errors.push({
          id: 1,
          error: "El nombre del centro es obligatorio",
        });
      }
      if (!this.address) {
        this.errors.push("La dirección del centro es obligatoria");
      }
      if (!this.phone) {
        this.errors.push("El teléfono del centro es obligatorio");
      }
      if (!this.email) {
        this.errors.push("El email del centro es obligatorio");
      }
      if (!this.open_time) {
        this.errors.push("El horario de apertura del centro es obligatorio");
      }
      if (!this.open_close) {
        this.errors.push("El horario de cierre del centro es obligatorio");
      }
      if (!this.municipality) {
        this.errors.push("El municipio del centro es obligatorio");
      }
      if (!this.open_time) {
        this.errors.push("El tipo de centro es obligatorio");
      }
    },

    createCenter() {
      console.log(this.center);
      this.sendCenter(this.center);
    },

    sendCenter(center) {
      axios.post("http://localhost:5000/centros", center).then((response) => {
        console.log(response);
      });
    },
    listMunicipios() {
      axios
        .get(
          "https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios?per_page=135"
        )
        .then((response) => {
          let result = [];
          for (var i = 1; i <= 135; i++) {
            result.push(response.data.data.Town[i].name);
          }
          this.municipalitys = result;
        });
    },
  },

  mounted() {
    this.listMunicipios();
  },
};
</script>