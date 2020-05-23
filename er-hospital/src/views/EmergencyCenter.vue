<template>
    <v-content>
        <v-container
                class="fill-height"
                fluid
        >
            <v-row
                    align="left"
                    justify="center"
            >
                <v-col
                        cols="12"
                        sm="8"
                        md="4"
                >
                    <v-card class="elevation-1">
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>Emergency Video Call</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-container v-if="!mode">
                            <v-card-text >
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
                        </v-container>
                        <v-container v-else>
                            <v-container v-if="mode==='sending'">
                                    SMS being sent to {{number}}
                            </v-container>
                            <v-container v-else>
                                <v-card-text >
                                   <div></div>
                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="primary">Send SMS</v-btn>
                                </v-card-actions>

                            </v-container>

                        </v-container>

                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-content>
</template>

<script>
    export default {
        name: "EmergencyCenter",
        data() {
            return {
                mode: null,
                number: ""
            }
        },
        methods: {
            sendSMS: function() {

            }
        }
    }
</script>

<style scoped>

</style>