<template>
  <div>
    <v-data-table :items="waiting" :headers="headers" :class="$style.table">
      <template v-slot:item.priorityType="{ item }">
        <v-icon :color="item.priorityType === 'P1' ? 'red' : 'teal'">
          keyboard_arrow_up
        </v-icon>
      </template>
      <template v-slot:item.arrived="{ item }">
        <v-btn v-if="!item.arrived" @click="showDialog = true">Anrufen</v-btn>
      </template>
    </v-data-table>
    <v-dialog v-model="showDialog">
      <v-card>
        <v-card-title>Wir verbinden Sie...</v-card-title>
        <v-card-text>
          <div>INSERT JITSI</div>
          <v-text-field v-model="notes"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn>Auflegen</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'CallCenter',
  data() {
    return {
      notes: 'Das ist ein nützlicher Anamnese-Text',
      showDialog: false,
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
          text: 'Anrufen',
          value: 'arrived',
        },
      ]
    },
  },
})
</script>

<style lang="scss" module>
  .table {
    padding-top: 4rem;
    width: 80vw;
  }
</style>

