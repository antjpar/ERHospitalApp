<template>
  <v-app id="inspire">
    <v-app-bar app color="indigo" dark>
      <v-toolbar-title>Hospital App</v-toolbar-title>
    </v-app-bar>

    <div :class="$style.sheet">
      <router-view />
    </div>

    <v-bottom-navigation fixed>
      <v-btn to="/">
        Dashboard
        <v-icon>dashboard</v-icon>
      </v-btn>
      <v-btn link to="/waiting-room">
        Waiting Room
        <v-icon>group</v-icon>
      </v-btn>
      <v-btn link to="/call-center">
        Call Center
        <v-icon>phone_in_talk</v-icon>
      </v-btn>
      <v-btn link to="/emergency">
        Emergency Room
        <v-icon>videocam</v-icon>
      </v-btn>
      <v-btn icon="assignment" link to="/checkin">
        Check-In
        <v-icon>assignment</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
export default {
  props: {
    source: String,
  },
}
</script>

<style module lang="scss">
.sheet {
  display: grid;
  justify-items: center;
  align-items: center;
}
</style>
