<template>
    <div class="genre">
        <table v-for="(genre, index) in genres" v-bind:key="genre.id">
            <thead>
                <th><h2>Genre</h2></th>
            </thead>
            <tr>
                <td><input v-model="genre.name" class="genre_name"/></td>
                <td><button class="del" v-on:click="del(index)">Delete</button></td>
            </tr>
            <tr><Category></Category></tr>
        </table>
        <button class="add" v-on:click="add">Add</button>
    </div>
</template>

<script>
    import Category from './CategoryInput.vue'
    export default {

        data() {
            return {
                genres:[{name:''}]
            }
        },
        components:{
            Category
        },

        methods:{
            add: function(){
                this.genres.push({name:''})
            },
            del: function(index){
                console.log(index);
                console.log(this.genres);
                this.genres.splice(index,1);
            },
        }
    }
</script>
<style>
    .genre_name {
        padding: 0.5em 1em;
        font-weight: bold;
        border: solid 3px;
    }
    .del {
        padding: 0.5em 1em;
        font-weight:bold;
        font-size:20px;
        color: white;
        background-color: red;
    }
    .add {
        padding:0.5em 1em;
        font-weight: bold;
        font-size:20px;
        color:white;
        background-color: greenyellow;
    }
    .category_name {
        padding: 0.5em 1em;
        margin: 0 5em;
        font-weight:bold;
        font-size:20px;
        border: solid 3px;
    }
</style>