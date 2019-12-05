<template>
  <div class="card" >
    <img v-if="item.image" class="card-img-top" alt="Card image cap" :src="item.image"/>
    <div class="card-body">
      <h4 class="card-title">{{item.productname}}</h4>
      <p class="card-text">
        {{item.description}}
      </p>
      <router-link to="/detail" :id="item.product_no" class="btn btn-primary">Detail</router-link>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    item: Object,
  }

};
</script>
<style></style>
