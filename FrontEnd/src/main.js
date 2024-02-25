import './assets/css/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'


const app = createApp(App)
const vuetify = createVuetify({
  components,
  directives,
})

app.mixin({
  data() {
    return {
      API_URL: 'http://127.0.0.1:5000/api',
      DATA_URL: 'http://127.0.0.1:3000'
    }
  },
})

app.use(router)
app.use(vuetify)
app.mount('#app')
