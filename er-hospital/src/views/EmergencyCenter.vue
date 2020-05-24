<template>
  <v-card :class="$style.emergencyVideoCall">
    <v-card-title>Emergency Video Call</v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field
          label="Mobile Number"
          name="mobile"
          prepend-icon="phone"
          type="text"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="primary">Send SMS</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'EmergencyCenter',
  data() {
    return {
      mode: null,
      number: '',
    }
  },
  methods: {
    sendSMS: function () {},
  },
}
</script>

<style lang="scss" module>
  .emergencyVideoCall {
    max-width: 60vw;
    max-height: 30vh;
    position: fixed;
    top: 5rem;
  }
</style>
