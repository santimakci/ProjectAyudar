<template>
  <div>
    <v-card class="pa-md-4 mx-lg-auto" style="width: 60%; margin: auto">
      <form @submit.prevent="createTurn" id="new-turn">

        <v-text-field
          v-model="turn.email"
          label="E-mail"
          @input="$v.turn.email.$touch()"
          @blur="$v.turn.email.$touch()"
        ></v-text-field>  

        <v-text-field
          v-model="turn.phone"
          label="Teléfono"
          type="number"
          @input="$v.turn.phone.$touch()"
          @blur="$v.turn.phone.$touch()"
        ></v-text-field>

        <v-select
          v-model="turn.time"
          :items="available_times"
          label="Seleccione un horario"
          @input="$v.turn.time.$touch()"
          @blur="$v.center.time.$touch()"
        ></v-select>

        <v-select
          v-model="turn.day"
          :items="available_days"
          label="Seleccione un dia"
          @input="$v.turn.time.$touch()"
          @blur="$v.center.time.$touch()"
        ></v-select>

        <v-row justify="center">
          <v-btn type="submit" form="new-turn" class="primary">
            Crear turno
          </v-btn>
        </v-row>
      </form>
    </v-card>
    <br />
  </div>
</template>

<script>


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
        time: "",
      },
    };
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
      time: {
        required,
      },
      day: {
        required,
      },
    },
  },

  computed: {

  },

  methods: {

  },

};
</script>