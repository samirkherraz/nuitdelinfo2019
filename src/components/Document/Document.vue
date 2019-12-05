<template>
    <div class="card-columns">
        <div class="card bg-dark mr-md-3 pt-3 px-3 pt-md-5 px-md-5 text-white overflow-hidden">
            <div class="my-3 py-3">
                <h2 class="display-5">Identité</h2>
                <p class="lead">Description</p>
            </div>
          <div v-if="document.image !== undefined" class="bg-light shadow-sm sized" >
              <img :src="document.image" class="img-fluid" alt="">
          </div>
       </div>
    </div>
</template>

<script>
    export default {
        props : {

            //image : image
            document : {
                titre:"titre",
                image:"https://helpx.adobe.com/content/dam/help/en/stock/how-to/visual-reverse-image-search/jcr_content/main-pars/image/visual-reverse-image-search-v2_intro.jpg",
                description:"description"
            },
        },
        mounted() {
            console.log(this.document)
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