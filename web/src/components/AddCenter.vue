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
          label="Nombre del centro *"
          @input="$v.center.name.$touch()"
          @blur="$v.center.name.$touch()"
        ></v-text-field>
        <v-text-field
          v-model="center.address"
          :error-messages="addressErrors"
          label="Dirección"
          @input="$v.center.address.$touch()"
          @blur="$v.center.address.$touch()"
        ></v-text-field>
        <v-text-field
          v-model="center.phone"
          label="Teléfono"
          :error-messages="phoneErrors"
          type="number"
          @input="$v.center.phone.$touch()"
          @blur="$v.center.phone.$touch()"
        ></v-text-field>
        <v-text-field
          v-model="center.email"
          :error-messages="emailErrors"
          label="E-mail"
          @input="$v.center.email.$touch()"
          @blur="$v.center.email.$touch()"
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
        <v-text-field v-model="center.web" label="Página web"></v-text-field>
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
import { required, email } from "vuelidate/lib/validators";

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
  validations: {
    center: {
      name: {
        required,
      },
      email: {
        email,
        required,
      },
      phone: {
        required,
      },
      address: {
        required,
      },
    },
  },

  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.center.email.$dirty) return errors;
      !this.$v.center.email.email && errors.push("Debería ser un email");
      !this.$v.center.email.required && errors.push("El email es requerido");
      return errors;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.center.name.$dirty) return errors;
      !this.$v.center.name.required &&
        errors.push("El nombre del centro es obligatorio");
      return errors;
    },
    phoneErrors() {
      const errors = [];
      if (!this.$v.center.phone.$dirty) return errors;
      !this.$v.center.phone.required &&
        errors.push("El teléfono es obligatorio");

      return errors;
    },
    addressErrors() {
      const errors = [];
      if (!this.$v.center.address.$dirty) return errors;
      !this.$v.center.address.required &&
        errors.push("La direccion es obligatoria");
      return errors;
    },
  },

  methods: {
    createCenter() {
      axios
        .post("http://localhost:5000/centros", this.center)
        .then((response) => {
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