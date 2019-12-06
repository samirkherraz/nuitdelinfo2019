<template>
    <form enctype="multipart/form-data" v-on:change="uploadFile($event)">
        <div class="form-group">
            <label :for="input.name">{{ input.type }}</label>
            <input type="file" :id="input.id" :name="input.name" :value="input.name"/>
        </div>
    </form>

</template>

<script>
    export default {
        props : {
            input: Object

        },
        methods:{
            uploadFile(event){
                const file = event.targe.files[0];
                this.$orchestra.putDocument(function () {
                    alert("Yes on l'a envoyé, et on s'est arrêté là, désolé ...");
                }, file);
            }
        }
    }
</script>