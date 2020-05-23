<template>
    <v-app id="inspire">
      <v-navigation-drawer
              v-model="drawer"
              app
      >
        <v-list dense>
          <v-list-item link :to="{path:'/'}">
            <v-list-item-action>
              <v-icon>dashboard</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item link :to="{path:'/waiting-room'}">
            <v-list-item-action>
              <v-icon>group</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Waiting Room</v-list-item-title>
            </v-list-item-content>
          </v-list-item><v-list-item link :to="{path:'/call-center'}">
            <v-list-item-action>
              <v-icon>phone_in_talk</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Call Center</v-list-item-title>
            </v-list-item-content>
          </v-list-item><v-list-item link :to="{path:'/emergency'}">
            <v-list-item-action>
              <v-icon>videocam</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Emergency Room</v-list-item-title>
            </v-list-item-content>
          </v-list-item><v-list-item link :to="{path:'/checkin'}">
            <v-list-item-action>
              <v-icon>assignment</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Check-In</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-app-bar
              app
              color="indigo"
              dark
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Hospital App</v-toolbar-title>
      </v-app-bar>

      <v-content>
        <v-container
                class="fill-height"
                fluid
        >
          <v-row
                  align="center"
                  justify="center"
          >
            <v-col class="text-center">
              <router-view/>
            </v-col>
          </v-row>
        </v-container>
      </v-content>
      <v-footer
              color="indigo"
              app
      >
        <span class="white--text">&copy; 2019</span>
      </v-footer>
    </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
    }),
  }
</script>