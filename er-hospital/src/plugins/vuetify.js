import 'material-design-icons-iconfont/dist/material-design-icons.css'

import Vue from 'vue';
import Vuetify from 'vuetify/lib';

import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
    icons: {
        iconfont: 'md',
    },
    theme: {
        themes: {
            inspire: {
                primary:colors.green.darken1,
                secondary: colors.green.lighten4,
                accent: colors.indigo.base
            }
        }
    }
});
