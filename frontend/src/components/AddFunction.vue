<template>
    <div class="add_test">
        <table class="table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th colspan="2">Address</th>
                </tr>
            </thead>
            <t-body>
                <tr v-for="(user, index) in users" v-bind:key="user.id">
                    <td><input v-model="user.name"/></td>
                    <td><input v-model="user.mail" /></td>
                    <td class="last"><button v-on:click="del(index)">Delete</button></td>
                </tr>
            </t-body>
        </table>
        <button class="add" v-on:click="add">Add</button>
    </div>
</template>

<style>
    * {
        box-sizing: border-box;
    }

    #add_test {
        width: 96%;
        max-width: 500px;
        margin: 40px auto;
        padding: 28px;
            border: 1px solid #ffffff;
            border-radius: 5px;
            background-color: transparent;
            box-shadow: 2px 2px 5px 0px rgba(200, 200, 200, 1);
            font-family: "Times New Roman";
    }

    .table {
        display: table;
        width: 100%;
        thead {
            tr {

                th {
                    padding: 8px;
                    text-align: left;
                    font-size: 12px;
                    color: #fff;
                    background-color: #384878;
                }
            }
        }
        tbody {
            tr {
                border-bottom: 1px solid #bcbcbc;
                td {
                    display: table-cell;
                    width: 43%;
                    padding: 8px;
                    &.last {
                        width: 80px;
                    }
                    input {
                        width: 100%;
                    }
                    button {
                        border: 0;
                        border-radius: 5px;
                        box-shadow: none;
                        color: #fff;
                        background-color: red;
                        cursor: pointer;
                    }
                }
            }
        }
    }

    .add {
        border: 0;
        box-shadow: none;
        color: #fff;
        background-color: #00c2bc;
        cursor: pointer;
    }
</style>

<script>
    export default({
        el:'#add_test',
        data() {
            return {
                users:[{name:'', mail:''}]
            }
        },
        methods: {
            add: function(){
                this.users.push({name:'', mail:''})
            },
            del: function(index){
                this.users.splice(index,1)
            }
        }
    })

</script>