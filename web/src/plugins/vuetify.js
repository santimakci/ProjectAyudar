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
        error: '#ff3333',
        info: '#29b6f6',
        success: '#00ff00',
        warning: '#FFCC00',
        anchor: '#ffffff'
      },
    },
  },
  icons: {
    iconfont: 'mdi', // default - only for display purposes
  },
});