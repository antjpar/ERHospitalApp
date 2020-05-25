<template>
    <div>
        <v-card :class="$style.emergencyVideoCall">
            <v-card-title>Emergency Video Call</v-card-title>
            <v-card-text>
                <v-form @submit="submit">
                    <v-text-field
                            ref="number"
                            label="Mobile Number"
                            name="mobile"
                            prepend-icon="phone"
                            type="text"
                            v-model="number"
                            :error-messages="errorMessage"
                    ></v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="callUser" :disabled="!isValid">Send SMS</v-btn>
            </v-card-actions>
        </v-card>
        <v-dialog v-model="showDialog">
            <v-card>
                <v-card-title>Wir verbinden Sie...</v-card-title>
                <v-card-text>
                    <div ref="jitsi" :class="$style.emergencyVideoContainer"></div>
                    <v-text-field v-model="notes"></v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-btn @click="showDialog = false">Auflegen</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>

   import Jitsi from '../jitsi'
   import uuid from 'uuid-random'


    export default {
        name: 'EmergencyCenter',
        data() {
            return {
                mode: null,
                showDialog: false,
                number: '',
                roomName: null,
                domain: "call.parsons.group",
                api: null
            }
        },
        computed: {
            isValid: function() {
                /* eslint-disable */
                const numberRegex = new RegExp(/^([\+][0-9]{1,3}[ \.\-])?([\(]{1}[0-9]{1,6}[\)])?([0-9 \.\-\/]{3,20})((x|ext|extension)[ ]?[0-9]{1,4})?$/)
                return numberRegex.test(this.number);
            },
            errorMessage: function() {
                return (this.number.length >0 && !this.isValid) ?'The number is not a valid mobile number!' : '';
            },
            callURL: function () {
                return "https://"+this.domain+'/'+this.roomName;
            }
        },
        methods: {
            sendSMS: function () {
                //Send the SMS
            },
            callUser: function () {
                this.roomName= uuid()
                this.sendSMS()
                this.showDialog = true;
            },
            submit: function(e) {
                if (this.isValid) {
                    this.callUser()
                }
                e.preventDefault();
            }
        },
        watch: {
            showDialog: function () {
            }
        },
        updated() {
            if (this.showDialog) {
                if (this.$refs.jitsi && !this.api) {
                this.$refs.jitsi.innerHTML ='';
                this.api = new Jitsi(this.domain, {
                        roomName: this.roomName,
                        width: 600,
                        height: 400,
                        parentNode: this.$refs.jitsi
                    })
            }
            } else {
                this.api.executeCommand('hangup')
                this.$refs.jitsi
                this.api = null;
            }
        }
    }
</script>

<style lang="scss" module>
    .emergencyVideoCall {
        max-width: 60vw;
        max-height: 30vh;
        position: fixed;
        top: 5rem;
    }
    .emergencyVideoContainer {
        text-align: center;
    }
</style>
