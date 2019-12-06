
import Vue from "vue";
import Vuex from "vuex";
import Constants from "@/constants/constants";

Vue.use(Vuex);

let state = { // données membres
    person : {},
    documents : [],
    categories: [],
    proccat: [],
    filter: Constants.NONE_VALUE,
    demarche: Constants.NONE_VALUE,
    demarches: [],
    inputs: []
};

export default new Vuex.Store({
    state,

    mutations: { // Modifiers
        addDocument :   (state, document) => state.documents.push(document),
        documents :   (state, documents) => state.documents =documents,
        demarches :   (state, demarches) => state.demarches =demarches,
        inputs :   (state, inputs) => state.inputs =inputs,
        resetFilter :   state             => state.filter = Constants.NONE_VALUE,
        setFilter :     (state, filter)   => state.filter = filter === ""? Constants.NONE_VALUE : filter,

        categories:  (state, data)             => state.categories = data,
        resetDemarche:  state             => state.demarche = Constants.NONE_VALUE,
        setDemarche:    (state, demarche) => state.demarche = demarche === ""? Constants.NONE_VALUE : demarche
    },

    getters : {
        inputs :     state => state.inputs,
        documents :     state => state.documents,
        categories:     state => state.categories,
        demarches:         state => state.demarches,
        filter :        state => state.filter,
        hasFilter :     state => (state.filter !== Constants.NONE_VALUE),
        proccat:        state => state.proccat,
        demarche :     state => state.demarche,
        hasDemarche :   state => (state.demarche !== Constants.NONE_VALUE),
    },

    mounted(){

    }
});