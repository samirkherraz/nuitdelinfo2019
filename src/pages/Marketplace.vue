<template>
  <div class="container-fluid">
    <filters />
    <div class="card-columns">
      <product v-for="item in products" v-bind:key="item.product_no" :item="item" />
    </div>
  </div>
</template>

<script>
import Filters from "@/components/Marketplace/Filters.vue";
import Product from "@/components/Marketplace/Product.vue";

export default {
  components: { Filters, Product },
  data() {
    return { products: [] };
  },
  mounted() {
    this.$orchestra.getProducts(data => {
      this.products = data;
    });
  }
};
</script>
<style></style>
