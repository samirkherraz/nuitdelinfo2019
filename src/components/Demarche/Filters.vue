<template>
    <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid">
            <div class="collapse navbar-collapse">
                <form class="navbar-nav">
                    <div class="input-group  mr-2">

                        <div class="input-group-prepend">
                            <label class="input-group-text">Démarches</label>
                        </div>

                        <select @change="onCategorySelect($event)" class="custom-select">
                            <option :value="NONE_VALUE" selected>Choisissez une démarche ...</option>
                            <option v-for="item in demarches" :value="item.id">item.name</option>
                        </select>
                    </div>
                </form>
            </div>
        </div>
    </nav>
</template>
<script>
    import store from "@/store/store";
    import Constants from "@/constants/constants";

    export default {
        props : {
            demarches : [],
            NONE_VALUE: Constants.NONE_VALUE
        },
        mounted() {
            store.commit("resetDemarche");
            this.demarches = store.getters.demarches
        },
        methods : {
            onCategorySelect(event) {
                store.commit("setDemarche", event.target.value);
            }
        }
    }
</script>