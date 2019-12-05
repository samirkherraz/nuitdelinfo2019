import axios from "axios";
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X_XSRF_TOKEN'
axios.defaults.withCredentials = true
export default {
  install(Vue) {
    
    class Nuitdelinfo {
     

      getProducts(callback) {
        axios
          .get("http://127.0.0.1:8000/api/product/all")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            error(e);
          });
      }
      
    }
    let nuitdelinfo = new Nuitdelinfo();
    Vue.nuitdelinfo = nuitdelinfo;
    Vue.prototype.$nuitdelinfo = nuitdelinfo;
  }
};
