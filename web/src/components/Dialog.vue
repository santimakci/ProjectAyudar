<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <template flat v-slot:activator="{ on, attrs }">
      <v-btn @click="show" color="primary" dark v-bind="attrs" v-on="on">
        Solicitar turno
      </v-btn>
    </template>
    <v-card>
      <div v-if="message.submitted">
        <v-alert v-if="message.type == 201" type="success">
          {{ message.text }}
        </v-alert>
        <v-alert v-else type="warning">
          {{ message.text }}
        </v-alert>
      </div>
      <v-card-title class="headline">
        <h2>Solicitar turno</h2>
      </v-card-title>
      <v-card-subtitle>
        <br />
        <h3>
          Para el centro <i>{{ center.name }}</i>
        </h3>
      </v-card-subtitle>
      <form v-on:submit.prevent="createTurn" id="new-turn">
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6">
                <v-text-field
                  label="Nombre *"
                  v-model="turn.name"
                  id="name"
                  :error-messages="nameErrors"
                  required
                  @input="$v.turn.name.$touch()"
                  @blur="$v.turn.name.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field
                  v-model="turn.lastname"
                  label="Apellido *"
                  :error-messages="lastnameErrors"
                  required
                  @input="$v.turn.name.$touch()"
                  @blur="$v.turn.name.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="turn.email"
                  label="Email *"
                  :error-messages="emailErrors"
                  required
                  @input="$v.turn.email.$touch()"
                  @blur="$v.turn.email.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="turn.phone"
                  label="Teléfono *"
                  type="number"
                  :error-messages="phoneErrors"
                  required
                  @input="$v.turn.phone.$touch()"
                  @blur="$v.turn.phone.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-menu
                  ref="menu"
                  :close-on-content-click="false"
                  :return-value.sync="day"
                  transition="scale-transition"
                  offset-y
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="turn.day"
                      label="Fecha"
                      :error-messages="dayErrors"
                      prepend-icon="mdi-calendar"
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="turn.day"
                    :min="nowDate"
                    no-title
                    scrollable
                  >
                    <v-spacer></v-spacer>
                    <v-btn text color="primary" @click="menu = false">
                      Cancel
                    </v-btn>
                    <v-btn
                      text
                      color="primary"
                      @click="$refs.menu.save(day), loadTurns()"
                      @input="$v.turn.day.$touch()"
                      @blur="$v.turn.day.$touch()"
                    >
                      OK
                    </v-btn>
                  </v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="12" sm="6">
                <v-select
                  v-model="turn.time"
                  :items="turns"
                  :error-messages="timeErrors"
                  required
                  label="Turno"
                  @input="$v.turn.time.$touch()"
                  @blur="$v.turn.time.$touch()"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false"> Cerrar </v-btn>
          <v-btn
            color="primary"
            text
            type="submit"
            form="new-turn"
            @click="dialog = false"
          >
            Confirmar
          </v-btn>
        </v-card-actions>
      </form>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";

import { required, email } from "vuelidate/lib/validators";

export default {
  name: "AddTurn",
  data() {
    return {
      nowDate: new Date().toISOString().slice(0, 10),
      turns: [],
      turns_submitted: false,
      turn: {
        name: "",
        lastname: "",
        email: "",
        phone: "",
        day: new Date().toISOString().substr(0, 10),
        time: "",
      },
      dialog: false,
      message: {
        type: "",
        text: "",
        submitted: false,
      },
    };
  },
  props: {
    center: Object,
  },
  validations: {
    turn: {
      name: {
        required,
      },
      lastname: {
        required,
      },
      email: {
        email,
        required,
      },
      phone: {
        required,
      },
      day: {
        required,
      },
      time: {
        required,
      },
    },
  },
  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.turn.email.$dirty) return errors;
      !this.$v.turn.email.required &&
        errors.push("El email del solicitante es obligatorio");
      !this.$v.turn.email.email && errors.push("Debería ser un email");
      return errors;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.turn.name.$dirty) return errors;
      !this.$v.turn.name.required &&
        errors.push("El nombre del solicitante del turno es obligatorio");
      return errors;
    },
    phoneErrors() {
      const errors = [];
      if (!this.$v.turn.phone.$dirty) return errors;
      !this.$v.turn.phone.required && errors.push("El teléfono es obligatorio");
      return errors;
    },
    lastnameErrors() {
      const errors = [];
      if (!this.$v.turn.lastname.$dirty) return errors;
      !this.$v.turn.lastname.required &&
        errors.push("El apellido del solicitante es obligatorio");
      return errors;
    },
    timeErrors() {
      const errors = [];
      if (!this.$v.turn.time.$dirty) return errors;
      !this.$v.turn.time.required &&
        errors.push("El horario del turno es obligatorio");
      return errors;
    },
    dayErrors() {
      const errors = [];
      if (!this.$v.turn.day.$dirty) return errors;
      !this.$v.turn.day.required &&
        errors.push("La fecha del turno es obligatoria");
      return errors;
    },
  },
  methods: {
    show() {
      this.$emit("showOff", false);
    },
    loadTurns() {
      axios
       /* .get(
          "https://admin-grupo21.proyecto2020.linti.unlp.edu.ar/centers" +
            this.center.id +
            "/turnos_disponibles/" +
            String(this.turn.day)
        )*/
         .get(
          "http://localhost:5000/centers/" +
            this.center.id +
            "/turnos_disponibles/" +
            String(this.turn.day)
        )
        .then((response) => {
          this.turns = [];
          console.log(this.turns);
          for (var i = 1; i <= Object.keys(response.data).length; i++) {
            if (response.data[i] in window == false)
              this.turns.push(response.data[i]);
          }
          console.log(this.turns);
        });
    },
    createTurn() {
      axios
        /*.post(
          "https://admin-grupo21.proyecto2020.linti.unlp.edu.ar/centers/" +
            this.center.id +
            "/reserva",
          this.turn
        )*/
        .post(
          "http://localhost:5000/centers/" +
            this.center.id +
            "/reserva",
          this.turn
        )
        .then((response) => {
          this.turn.name = "";
          this.turn.lastname = "";
          this.turn.email = "";
          this.turn.phone = "";
          this.turn.day = new Date().toISOString().substr(0, 10);
          this.turn.time = "";
          this.$emit("superMSJ", response.data);
        });
    },
    resetInputs() {
      this.turn.name = "";
      this.turn.lastname = "";
      this.turn.email = "";
      this.turn.phone = "";
      this.turn.day = new Date().toISOString().substr(0, 10);
      this.turn.time = "";
    },
  },
};
</script>
