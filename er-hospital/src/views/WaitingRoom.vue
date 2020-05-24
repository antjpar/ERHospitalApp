<template>
  <div :class="$style.table">
    <v-btn icon outlined :class="$style.plusButton" large>
      <v-icon color="white">add</v-icon>
    </v-btn>
    <v-data-table :items="waiting" :headers="headers">
      <template v-slot:item.priorityType="{ item }">
        <v-icon :color="item.priorityType === 'P1' ? 'red' : 'teal'">
          keyboard_arrow_up
        </v-icon>
      </template>
      <template v-slot:item.arrived="{ item }">
        <v-btn v-if="!item.arrived">BESTÄTIGEN</v-btn>
      </template>
      <template v-slot:item.treated="{ item }">
        <v-btn v-if="!item.arrived">BEHANDELT</v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'WaitingRoom',
  data() {
    return {
      waiting: [
        {
          id: 1,
          priorityType: 'P1',
          firstname: 'Leila',
          lastname: 'Mustermann',
          birthdate: '1980-10-12',
          arrived: false,
          treated: false,
        },
        {
          id: 0,
          priorityType: 'P2',
          firstname: 'Max',
          lastname: 'Mustermann',
          birthdate: '1980-10-12',
          arrived: false,
          treated: false,
        },
      ],
    }
  },
  computed: {
    headers() {
      return [
        { text: '', value: 'priorityType' },
        {
          text: 'Vorname',
          value: 'firstname',
        },
        {
          text: 'Nachname',
          value: 'lastname',
        },
        {
          text: 'Geburtsdatum',
          value: 'birthdate',
        },
        {
          text: 'Annahme',
          value: 'arrived',
        },
        {
          text: 'Behandelt',
          value: 'treated',
        },
      ]
    },
  },
})
</script>

<style lang="scss" module>
  .table {
    padding-top: 4rem;
    width: 80%;
  }
  .plusButton {
    position: fixed;
    bottom: 10vh;
    right: 5vw;
    background-color: #3f51b5;
  }
</style>
