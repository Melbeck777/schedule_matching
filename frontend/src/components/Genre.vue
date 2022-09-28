<template>
    <div class="genre">
        <table>
            <thead>
                <th>Genre</th>
            </thead>
            <tr v-for="(genre, index) in genres" v-bind:key="genre.id">
                <td><input v-model="genre.name"/></td>
                <td><Category></Category></td>
                <td><button class="del" v-on:click="del(index)"></button></td>
            </tr>
            <button class="add" v-on:click="add"></button>
        </table>
    </div>
</template>

<script>
    import Category from './CategoryInput.vue'
    export default {
        el:'#genre',
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
                this.genres.splice(index,1)
            },
        }
    }
</script>