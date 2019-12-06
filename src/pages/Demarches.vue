<template>
    <div>
        <Filters></Filters>

        <div v-if="demarche !== NONE_VALUE" class="card-columns" style="margin-top: 1rem">
            <demarche v-bind:demarche="demarche"></demarche>
            <Input v-for="input in inputs" v-bind:input="input"/>
            <button @click="soumettre" type="button" class="btn btn-primary">Soumettre</button>
        </div>
    </div>
</template>

<script>
    import Input from "@/components/Demarche/Input.vue";
    import Demarche from "@/components/Demarche/Demarche.vue";
    import Filters from "@/components/Demarche/Filters.vue";
    import store from "@/store/store";
    import Constants from "@/constants/constants";

    export default {
        data() {
            return {
                demarche: Constants.NONE_VALUE,
                inputs: [],
                NONE_VALUE: Constants.NONE_VALUE
            }
        },
        components: {Filters, Demarche},
        mounted() {
            this.demarche = store.getters.demarche;
            this.inputs = store.getters.inputs;
        },
        computed: {
           
            soumettre: function () {
                for(inputId in inputs) {

                }
            }
        }

    }

</script>