<template>
    <div id="map"></div>
</template>

<link href='https://api.tiles.mapbox.com/mapbox-gl-js/v1.6.0/mapbox-gl.css' rel='stylesheet'/>

<script>
    import axios from 'axios';
    import mapboxgl from 'mapbox-gl';

    export default {
        data() {
            return {map: Object}
        },
        mounted() {
            mapboxgl.accessToken = 'pk.eyJ1Ijoia2V2aW4wNiIsImEiOiJjanU5eWt0Y3Ywb2hrNDRwZHFhdWJkcTcyIn0.wDK-JJjFVjytz9PlllbBaQ';
            this.map = new mapboxgl.Map({
                container: 'map', // container id
                style: 'mapbox://styles/mapbox/streets-v11',
                center: [4.8656, 45.782],
                zoom: 15
            });

            let objs = [{
                name: "test",
                address: "58 rue Descartes 69100 Villeurbanne",
                type: "alimentaire"
            }];

            for (let idObj in objs) {
                this.setMarker(objs[idObj]);
            }
        },
        methods: {
            setMarker: function (entite) {

                let color;

                switch (entite.type) {
                    case 'alimentaire':
                        color = "vert";
                        break;

                    case 'a':
                        color = "jaune";
                        break;

                    case 'b':
                        color = "bleu";
                        break;

                    case 'c':
                        color = "violet";
                        break;

                    default:
                        console.error(error);
                }

                console.log("https://api.mapbox.com/geocoding/v5/mapbox.places/"+ entite.address +".json?access_token=pk.eyJ1Ijoia2V2aW4wNiIsImEiOiJjanU5eWt0Y3Ywb2hrNDRwZHFhdWJkcTcyIn0.wDK-JJjFVjytz9PlllbBaQ");


                new mapboxgl.Marker() // initialize a new marker
                    // Modifier pour la couleur
                    .setLngLat([4.8656, 45.782]) // Marker [lng, lat] coordinates
                    .addTo(this.map);

                axios.get("https://api.mapbox.com/geocoding/v5/mapbox.places/"+ entite.address +".json?access_token=pk.eyJ1Ijoia2V2aW4wNiIsImEiOiJjanU5eWt0Y3Ywb2hrNDRwZHFhdWJkcTcyIn0.wDK-JJjFVjytz9PlllbBaQ", {
                    headers: {
                        'Access-Control-Allow-Origin': '*',
                    }
                })
                .then(function (response) {
                    // handle success

                    // placement du marqueur avec les coord
                })
                .catch(function (error) {
                    // handle error
                    console.error("Error : Couldn't set marker for entity : "+entite.name);
                });
            }
        }
    }
</script>

<style>
#map{

    width: 100%;
    height: 75vh;

}
</style>