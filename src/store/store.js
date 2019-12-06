
import Vue from "vue";
import Vuex from "vuex";
import Constants from "@/constants/constants";

Vue.use(Vuex);

let state = { // données membres
    person : {},
    documents : [],
    filter: Constants.NONE_VALUE,
    categories: []
};

export default new Vuex.Store({
    state,

    mutations: { // Modifiers
        addDocument :   (state, document) => state.documents.push(document),

        resetFilter :   state             => state.filter = Constants.NONE_VALUE,
        setFilter :     (state, filter)   => state.filter = filter === ""? Constants.NONE_VALUE : filter
    },

    getters : {
        documents :     state => state.documents,
        categories:     state => state.categories,

        filter :        state => state.filter,
        hasFilter :     state => (state.filter !== Constants.NONE_VALUE)
    },

    mounted(){
        this.$orchestra.getDocuments((docs)=>{state.documents = docs})
        this.$orchestra.getDocumentCategories((cats)=>{state.categories = cats})
    }
});