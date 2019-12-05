import SideBar from "@/components/SidebarPlugin";
import GlobalDirectives from "./globalDirectives";
// import "es6-promise/auto";


import APP from './api';
//css assets
import "bootstrap/dist/css/bootstrap.css";
import "@/assets/sass/paper-dashboard.scss";
import "@/assets/css/themify-icons.css";

export default {
  install(Vue) {
    Vue.use(GlobalDirectives);
    Vue.use(SideBar);
    Vue.use(APP);
  }
}
