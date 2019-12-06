<template>
    <div>
        <Filters></Filters>

        <div v-if="demarche !== NONE_VALUE" class="card-columns" style="margin-top: 1rem">
            <Demarche v-bind:demarche="demarche"></Demarche>
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
        },
        computed: {
            getInputs: function () {
                if(demarche !== this.NONE_VALUE)
                    inputs = this.$orchestra.getProcedureDocuments(function(data){
                        this.inputs = data;
                    }, this.demarche);
            },
            soumettre: function () {
                for(inputId in inputs) {

                }
            }
        }

    }

</script>