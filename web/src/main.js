import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import '@babel/polyfill'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'
import router from './router'
import Vuelidate from 'vuelidate'
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';
import VePie from 'v-charts/lib/pie.common'
import VeBar from 'v-charts/lib/bar.common'

Vue.config.productionTip = false
Vue.use(Vuelidate)
Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.component(VePie.name, VePie)
Vue.component(VeBar.name, VeBar)




new Vue({
 vuetify,
 router,
 render: h => h(App)
}).$mount('#app')


