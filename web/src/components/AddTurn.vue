<template>
  <div>
    <v-card class="pa-md-4 mx-lg-auto" style="width: 60%; margin: auto">
      <div class="text-body-1 mb-6"></div>
      <form @submit.prevent="createTurn" id="new-turn">
        <v-card-title>
          <span class="headline">Solicitar un turno</span>
        </v-card-title>
        <v-card-subtitle>
          <span> Para el centro: '{{ center.name }}'</span>
        </v-card-subtitle>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Nombre" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="Apellido"
                  required
                  hint="example of helper text only on focus"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="turn.email"
                  label="E-mail*"
                  required
                  @input="$v.turn.email.$touch()"
                  @blur="$v.turn.email.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="turn.phone"
                  label="Teléfono"
                  type="number"
                  required
                  @input="$v.turn.phone.$touch()"
                  @blur="$v.turn.phone.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-menu
                  ref="menu"
                  v-model="menu"
                  :close-on-content-click="false"
                  :return-value.sync="date"
                  transition="scale-transition"
                  offset-y
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="date"
                      label="Fecha"
                      prepend-icon="mdi-calendar"
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="date" no-title scrollable>
                    <v-spacer></v-spacer>
                    <v-btn text color="primary" @click="menu = false">
                      Cancel
                    </v-btn>
                    <v-btn
                      text
                      color="primary"
                      @click="$refs.menu.save(date), loadTurns()"
                    >
                      OK
                    </v-btn>
                  </v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="12" sm="6">
                <v-select
                  v-model="turnos"
                  :items="turns"
                  :error-messages="centerTypeErrors"
                  label="Turno"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>* todos los campos son requeridos</small>
        </v-card-text>
        <v-row justify="center">
          <v-btn type="submit" color="blue darken-1" text form="new-turn">
            Confirmar turno
          </v-btn>
        </v-row>
      </form>
    </v-card>
    <br />
  </div>
</template>

<script>
import axios from "axios";

import { required, email } from "vuelidate/lib/validators";

export default {
  name: "AddTurn",
  components: {},

  data() {
    return {
      turns: [],
      errors: [],
      available_times: [],
      available_days: [],
      date: "",
      turn: {
        //center_id: "",
        email: "",
        //num_block: "",
        phone: "",
        day: "",
        // time: "",
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
      email: {
        email,
        required,
      },
      phone: {
        required,
      },
      // time: {
      //   required,
      // },
      day: {
        required,
      },
    },
  },

  computed: {},

  methods: {
    loadTurns() {
      axios
        .get(
          "http://localhost:5000/centers/" +
            this.center.id +
            "/turnos_disponibles/?date=" +
            this.date
        )
        .then((response) => {
          this.turns = [];
          for (var i = 1; i <= Object.keys(response.data).length; i++) {
            this.turns.push(response.data[i]);
          }
        });
    },
    createTurn() {
      axios
        .post("http://localhost:5000/1/reserva", this.center)
        .then((response) => {
          console.log(response);
        });
    },
  },
};
</script>

<!--
<style scoped>
  .sangre{
    filter: hue-rotate(140deg);
  }
  .plasma{
    filter: hue-rotate(220deg);
  }
  .ropa{
    filter: hue-rotate(70deg);
  }
  .comida{
    filter: hue-rotate(300deg);
  }
</style>-->