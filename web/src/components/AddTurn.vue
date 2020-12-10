<template>
  <div>
    <v-card class="pa-md-4 mx-lg-auto" style="width: 60%; margin: auto">
    <div class="text-body-1 mb-6 ">
    </div>
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
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  label="Nombre"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
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
              <v-col
                cols="12"
                sm="6"
              >
              <v-select
                v-model="turn.day"
                :items="available_days"
                label="Fecha"
                required
                @input="$v.turn.time.$touch()"
                @blur="$v.center.time.$touch()"
              ></v-select>
              </v-col>
              <v-col
                cols="12"
                sm="6"
              >
                <v-autocomplete
                  :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                  label="Horarios"
                  multiple
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>* todos los campos son requeridos</small>
        </v-card-text>
          <v-row justify="center">
          <v-btn type="submit" color="blue darken-1" text form="new-turn" >
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
  components: {  },

  data() {
    return {
      errors: [],
      available_times:[],
      available_days:[],
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
     center:Object
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

  computed: {

  },

  methods: {
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