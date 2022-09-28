<template>
    <div class="category">
        <table>
            <thead>
                <th><h2>Category</h2></th>
            </thead>
            <tbody>
                <tr v-for="(category, index) in categories" v-bind:key="category.id">
                    <td><input v-model="category.name" class="category_name"/></td>
                    <td><button class="del mx-5" v-on:click="del(index)">Delete</button></td>
                </tr>
                <td><button class="add category_name mx-5" v-on:click="add">Add<br/>category</button></td>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                categories:[{name:''}]
            }
        },
        methods:{
            add: function(){
                console.log(this.categories);
                this.categories.push({name:''})
            },
            del: function(index) {
                this.categories.splice(index,1)
            }
        }
    }
</script>