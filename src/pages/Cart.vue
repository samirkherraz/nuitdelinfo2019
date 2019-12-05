<template>
  <div class="container-fluid">
    cart
  </div>
</template>
<script>
import Filters from "@/components/Marketplace/Filters.vue";
import Product from "@/components/Marketplace/Product.vue";

export default {
  props: {
    item: Object
  },
  components: { Filters, Product }
};
</script>
<style></style>
