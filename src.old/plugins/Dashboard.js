import APP from './api';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import BootstrapVue from 'bootstrap-vue'

export default {
  install(Vue) {
    Vue.use(BootstrapVue);
    Vue.use(APP);
  }
}
