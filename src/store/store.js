
import Vue from "vue";
import Vuex from "vuex";
import Constants from "@/constants/constants";

Vue.use(Vuex);

let state = { // données membres
    person : {},
    documents : [],
    categories: [],

    filter: Constants.NONE_VALUE,
    demarche: Constants.NONE_VALUE
};

export default new Vuex.Store({
    state,

    mutations: { // Modifiers
        addDocument :   (state, document) => state.documents.push(document),

        resetFilter :   state             => state.filter = Constants.NONE_VALUE,
        setFilter :     (state, filter)   => state.filter = filter === ""? Constants.NONE_VALUE : filter,

        resetDemarche:  state             => state.demarche = Constants.NONE_VALUE,
        setDemarche:    (state, demarche) => state.demarche = demarche === ""? Constants.NONE_VALUE : demarche
    },

    getters : {
        documents :     state => state.documents,
        categories:     state => state.categories,

        filter :        state => state.filter,
        hasFilter :     state => (state.filter !== Constants.NONE_VALUE),

        demarche :     state => state.demarche,
        hasDemarche :   state => (state.demarche !== Constants.NONE_VALUE),
    },

    mounted() {
        // TODO INIT PAR ORCHESTRA
    }
});