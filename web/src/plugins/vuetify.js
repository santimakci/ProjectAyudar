import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
      options: {
        customProperties: true,
      },
    themes: {
      light: {
        primary: '#2BBBAD',
        secondary: '#aa66cc',
        accent: '#81d4fa',
        error: '#f44336',
        info: '#29b6f6',
        success: '#b2ff59',
        warning: '#ffc107', 
        anchor: '#ffffff'
      },
    },
  },
  icons: {
    iconfont: 'mdi', // default - only for display purposes
  },
});
