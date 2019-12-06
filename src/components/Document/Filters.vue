<template>
  <nav class="navbar navbar-expand-lg navbar-light">
    <div class="container-fluid">
      <div class="collapse navbar-collapse">
        <form class="navbar-nav">
          <div class="input-group  mr-2">

            <div class="input-group-prepend">
              <label class="input-group-text">Categories</label>
            </div>

            <select @change="onCategorySelect($event)" class="custom-select">
              <option :value="NONE_VALUE" selected>Choisissez une catégorie ...</option>
              <option v-for="item in categories" :value="item.name">toto</option>
            </select>
          </div>

<!--          <div class="input-group mr-2">-->
<!--            <div class="input-group-prepend">-->
<!--              <label class="input-group-text">Prix Min</label>-->
<!--            </div>-->
<!--            <input type="number" class="form-control" aria-label="Prix Min"/>-->
<!--            <div class="input-group-append">-->
<!--              <span class="input-group-text">Euros</span>-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="input-group mr-2">-->
<!--            <div class="input-group-prepend">-->
<!--              <label class="input-group-text">Prix Min</label>-->
<!--            </div>-->
<!--            <input type="number" class="form-control" aria-label="Prix Max" />-->
<!--            <div class="input-group-append">-->
<!--              <span class="input-group-text">Euros</span>-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="col-auto">-->
<!--            <button type="submit" class="btn btn-light m-auto">-->
<!--              Appliquer-->
<!--            </button>-->
<!--          </div>-->
        </form>
      </div>
    </div>
  </nav>
</template>
<script>
  import store from "@/store/store";
  import Constants from "@/constants/constants";
export default {
  data() {
    return { categories: [], NONE_VALUE: Constants.NONE_VALUE };
  },
  mounted() {
    store.commit("resetFilter");
    this.categories = store.getters.categories;
  },
  methods: {
    onCategorySelect(event) {
      store.commit("setFilter", event.target.value);
    }
  }
};
</script>
