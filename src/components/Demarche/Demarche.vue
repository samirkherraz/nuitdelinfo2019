<template>
    <div class="card bg-dark mr-md-3 pt-3 px-3 pt-md-3 px-md-5 text-white overflow-hidden">
        <div class="my-3 py-3">
            <h2 class="display-5">{{ demarche.name }}</h2>
            <p class="lead">{{ demarche.description }}</p>
        </div>
    </div>
</template>
<script>
    export default {
        props : {
            demarche: Object
        }
    }
</script>