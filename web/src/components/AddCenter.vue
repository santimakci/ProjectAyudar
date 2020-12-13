<template>
  <div>
      <div v-if="message.submitted"> 
      <v-alert v-if="message.type == 201" type="success">
        {{message.text}}
      </v-alert>
      <v-alert v-else type="warning">
        {{message.text}}
      </v-alert>    
    </div>
    <v-card class="pa-md-4 mx-lg-auto" style="width: 60%; margin: auto">
      <form    v-on:submit.prevent="checkIfRecaptchaVerified" id="new-center">
        <v-text-field
          v-model="center.name"
          id="name"
          required
          :error-messages="nameErrors"
          label="Nombre del centro *"
          @input="$v.center.name.$touch()"
          @blur="$v.center.name.$touch()"
        ></v-text-field>
        <v-row>
          <v-col cols="6">
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
                  required
                  :error-messages="openTimeErrors"
                  label="Hora de apertura *"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  @input="$v.center.open_time.$touch()"
                  @blur="$v.center.open_time.$touch()"
                ></v-text-field>
              </template>
              <v-time-picker
                v-model="time"
                full-width
                @click:minute="$refs.menu.save(time)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col cols="6">
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
                  required
                  :error-messages="closeTimeErrors"
                  label="Hora de cierre *"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  @input="$v.center.close_time.$touch()"
                  @blur="$v.center.close_time.$touch()"
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
        <v-text-field
          v-model="center.address"
          :error-messages="addressErrors"
          label="Dirección *"
          required
          @input="$v.center.address.$touch()"
          @blur="$v.center.address.$touch()"
        ></v-text-field>
        <v-text-field
          v-model="center.phone"
          label="Teléfono *"
          :error-messages="phoneErrors"
          required
          @input="$v.center.phone.$touch()"
          @blur="$v.center.phone.$touch()"
        ></v-text-field>
        <v-select
          v-model="center.center_type"
          :items="center_type"
          required
          :menu-props="{ top: true, offsetY: true }"
          :error-messages="centerTypeErrors"
          label="Tipo de centro *"
          @input="$v.center.center_type.$touch()"
          @blur="$v.center.center_type.$touch()"
        ></v-select>
        <v-select
          v-model="center.municipality"
          :items="municipalitys"
          required
          :menu-props="{ top: true, offsetY: true }"
          :error-messages="municipalityErrors"
          label="Municipalidad *"
          @input="$v.center.municipality.$touch()"
          @blur="$v.center.municipality.$touch()"
        ></v-select>
        <v-text-field
          v-model="center.email"
          :error-messages="emailErrors"
          label="Email"
          @input="$v.center.email.$touch()"
          @blur="$v.center.email.$touch()"
        ></v-text-field>
        <v-text-field v-model="center.web" label="Página web"></v-text-field>

        <MapSelectCenter v-on:sendLat="setLat" />
        <vue-recaptcha
          sitekey="6LcR5v8ZAAAAAJSsYo1aCCPM2Q0hK3___BkNo_w1 "
          ref="recaptcha" 
          @verify="markRecaptchaAsVerified"
          
        ></vue-recaptcha>
        
        <v-row  class="mt-5 ml-1">
          <v-btn type="submit" form="new-center" class="primary">
        
    Enviar centro
          </v-btn>
        </v-row>
      </form>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
import VueRecaptcha from "vue-recaptcha";
import { required, email } from "vuelidate/lib/validators";
import MapSelectCenter from "./MapSelectCenter"

export default {
  name: "AddCenter",
  components: { VueRecaptcha, MapSelectCenter },

  data() {
    return {
      errors: [],
      center_type: ["Alimentos", "Sangre", "Ropa", "Plasma"],
      municipalitys: [],
      captchaInfo:{
        recaptchaVerified: false,
        pleaseTickRecaptchaMessage: ''
      },
      center: {
        name: "",
        address: "",
        phone: "",
        open_time: "",
        close_time: "",
        center_type: "",
        municipality: "",
        latitude: "",
        longitude: "",
        email: "",
        web: "",
      },
      message: {
        type: "",
        text: "",
        submitted: false,
      }
    };
  },
  validations: {
    center: {
      name: {
        required,
      },
      email: {
        email,
      },
      phone: {
        required,
      },
      address: {
        required,
      },
      open_time: {
        required,
      },
      close_time: {
        required,
      },
      municipality: {
        required,
      },
      center_type: {
        required,
      },
    },
  },

  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.center.email.$dirty) return errors;
      !this.$v.center.email.email && errors.push("Debería ser un email");
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
    openTimeErrors() {
      const errors = [];
      if (!this.$v.center.open_time.$dirty) return errors;
      !this.$v.center.open_time.required &&
        errors.push("El horario de apertura es obligatorio");
      return errors;
    },
    closeTimeErrors() {
      const errors = [];
      if (!this.$v.center.close_time.$dirty) return errors;
      !this.$v.center.close_time.required &&
        errors.push("El horario de cierre es obligatorio");
      return errors;
    },
    municipalityErrors() {
      const errors = [];
      if (!this.$v.center.municipality.$dirty) return errors;
      !this.$v.center.municipality.required &&
        errors.push("La municipalidad es obligatoria");
      return errors;
    },
    centerTypeErrors() {
      const errors = [];
      if (!this.$v.center.center_type.$dirty) return errors;
      !this.$v.center.center_type.required &&
        errors.push("El tipo de centro es obligatorio");
      return errors;
    },
  },

  methods: {
    setLat(prop){
      this.center.latitude = prop.lat
      this.center.longitude = prop.lng
      console.log(this.center)
    },
    markRecaptchaAsVerified() {
      this.captchaInfo.pleaseTickRecaptchaMessage = '';
      this.captchaInfo.recaptchaVerified = true;
    },

    checkIfRecaptchaVerified() {
      if (!this.captchaInfo.recaptchaVerified) {
        alert('Please tick recaptcha.');
        return false; // prevent form from submitting
      }   
      this.createCenter()
    },
    createCenter() {
      axios
        .post("http://localhost:5000/centros", this.center)
        .then((response) => {
          console.log(response)
          this.message.submitted = true;
          this.message.type = response.data.status
          this.message.text = response.data.body
          
          
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