<template>
    <div>
        <Filters></Filters>

        <div class="card-columns" style="margin-top: 1rem">
            <Document v-if="doc.type === filter || filter == NONE_VALUE" v-for="doc in filteredDocumentsOrCategories" v-bind:document="doc" :key="doc.id"></Document>
        </div>
    </div>
</template>

<script>
    import store from "@/store/store";
    import Filters from "@/components/Document/Filters.vue";
    import Document from "@/components/Document/Document.vue";
    import Constants from "@/constants/constants";

    export default {
        data() {
            return {
                documents: Object,
                filter : "",
                NONE_VALUE: Constants.NONE_VALUE
            }
        },
        components: {Filters, Document},
        mounted() {
            this.documents = store.getters.documents;
            this.filter = store.getters.filter;
            console.log("filter : "+store.getters.filter);
           
        },

        computed: {
            filteredDocumentsOrCategories: function() {

                this.filter = store.getters.filter;

                return (store.getters.hasFilter)?
                    store.getters.documents :
                    store.getters.categories;
            }
        }
    }

</script>
