<template>
    <div class="card bg-dark mr-md-3 pt-3 px-3 pt-md-3 px-md-5 text-white overflow-hidden">
        <div class="my-3 py-3">
            <h2 class="display-5">{{ document.name }}</h2>
            <p class="lead">{{ document.description }}</p>
        </div>
      <div v-if="document.image !== undefined" class="bg-light shadow-sm sized" >
          <img :src="document.image" class="img-fluid" alt="">
      </div>
   </div>
</template>

<script>
    export default {
        props : {
            document: Object
        }
    }
</script>

<style>
    .sized {
        width: 80%;
        height: 30%;
        border-radius: 21px 21px 0 0;
    }
</style>