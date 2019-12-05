import Vue from "vue";
import App from "./App";
import router from "./router/index";
import Dashboard from "./plugins/Dashboard";
Vue.use(Dashboard);
new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
