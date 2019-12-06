import axios from "axios";
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X_XSRF_TOKEN'
axios.defaults.withCredentials = true
export default {
  install(Vue) {
    
    class Orchestra {
      sendMsg(callback, data) {
        axios
          .put("/api/chat/",{message: data})
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            error(e);
          });
      }

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
      getCategories(callback) {
        axios
          .get("http://127.0.0.1:8000/api/product/category")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            error(e);
          });
      }
      getCategory(callback, data) {
        axios
          .post("http://127.0.0.1:8000/api/product/category",data)
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            error(e);
          });
      }
    }
    let orchestra = new Orchestra();
    Vue.orchestra = orchestra;
    Vue.prototype.$orchestra = orchestra;
  }
};
