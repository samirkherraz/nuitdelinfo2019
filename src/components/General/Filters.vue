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
              <option selected>Choisissez une catégorie ...</option>
              <option v-for="item in categories" :value="item">{{item}}</option>
            </select>
          </div>

          <div class="input-group mr-2">
            <div class="input-group-prepend">
              <label class="input-group-text">Prix Min</label>
            </div>
            <input type="number" class="form-control" aria-label="Prix Min"/>
            <div class="input-group-append">
              <span class="input-group-text">Euros</span>
            </div>
          </div>

          <div class="input-group mr-2">
            <div class="input-group-prepend">
              <label class="input-group-text">Prix Min</label>
            </div>
            <input type="number" class="form-control" aria-label="Prix Max" />
            <div class="input-group-append">
              <span class="input-group-text">Euros</span>
            </div>
          </div>
          <div class="col-auto">
            <button type="submit" class="btn btn-light m-auto">
              Appliquer
            </button>
          </div>
        </form>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  data() {
    return { categories: [] };
  },
  mounted() {
    this.$orchestra.getCategories(data => {
      this.categories = data;
    });
  },
  methods: {
    onCategorySelect(event) {
      this.$orchestra.getCategory(data => {
        this.$parent.products = data
      },event.target.value );
    }
  }
};
</script>
