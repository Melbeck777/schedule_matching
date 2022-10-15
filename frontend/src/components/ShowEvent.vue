<template>
    <div class="genre">
        <v-row>
            <v-col v-for="genre in genres" v-bind:key="genre.id" class="genre_name">
                {{genre.name}}
                <div class="category">
                    <v-row v-for="category in genre.categories" v-bind:key="category.id" class="category ">
                        <v-col>{{category}}</v-col>
                    </v-row>
                </div>
            </v-col>
        </v-row>
    </div>
</template>

<script>
    export default {
        data:() => ({
            genres:[
                {name:'学年', categories:['教員','M2','M1','B4','B3']},
                {name:'研究室', categories:['制御','精密']}
            ]
        })
    }
</script>
<style>
    .category {
        margin: 5px;
        max-width: 100px;
        background-color: lightyellow;
        color:gray;
    }
    .genre {
        max-width: 300px;
        max-height: 10px;
        margin: auto;
    }

</style>