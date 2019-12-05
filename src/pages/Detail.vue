<template>
  <div class="container-fluid">
      <product :item="item" />
  </div>
</template>
<script>
import Product from "@/components/Marketplace/Product.vue";

export default {
  components: { Product },
  props: {
    item: Object,
  },
  data() {
    return { product: [] };
  },
  mounted() {
    this.$orchestra.getProducts(data => {
      this.item = data;
    });
  }
};
</script>
<style></style>
