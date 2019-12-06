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
            console.log(e);
          });
      }
      // Documents

      getDocuments(callback) {
        axios
          .get("/api/filedrop/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }

      getDocumentCategories(callback) {
        axios
          .get("/api/filedrop/category")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }

      getDocumentCategory(callback, id) {
        axios
          .get("/api/filedrop/category/"+id+"/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }

      downloadDocument(callback, id) {
        axios
          .get("/api/filedrop/binary/"+id+"/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }

      deleteDocument(callback, id) {
        axios
          .delete("/api/filedrop/"+id+"/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }

      updateDocument(callback, id, data) {
        axios
          .put("/api/filedrop/"+id+"/", data)
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }

      createDocument(callback, data) {
        axios
          .put("/api/filedrop/",data)
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }
      // Procedures
      getProcedures(callback) {
        axios
          .get("/api/procedure/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }
      getProcedureCategories(callback) {
        axios
          .get("/api/procedure/category")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }
      getProcedure(callback, id) {
        axios
          .get("/api/procedure/"+id+"/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }
      getProcedureDocuments(callback, id) {
        axios
          .get("/api/procedure/document/"+id+"/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }
      getProcedureCategory(callback, id) {
        axios
          .get("/api/procedure/category/"+id+"/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }
      
      getProcedureConstraint(callback, id) {
        axios
          .get("/api/procedure/constraint/"+id+"/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }

      checkProcedureConstraint(callback, id, data) {
        axios
          .post("/api/procedure/constraint/"+id+"/", data)
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }
      // Plan
      getPlans(callback) {
        axios
          .post("/api/plan/")
          .then(e => {
            callback(e.data.content);
          })
          .catch(e => {
            console.log(e);
          });
      }
      

    }
    let orchestra = new Orchestra();
    Vue.orchestra = orchestra;
    Vue.prototype.$orchestra = orchestra;
  }
};
