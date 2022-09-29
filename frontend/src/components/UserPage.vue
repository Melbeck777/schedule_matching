<template>
    <div class="user">
        <img src="../assets/Logo2_cat.jpeg" justify="center"/>
        <v-btn class="create" v-on:click="create_event">Create<br/>Event</v-btn>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name:'UserPage',
        data:() => ({
            user:[]
        }),
        mounted () {
            this.fetchData()
        },
        methods: {
            fetchData(){
                axios.get('/create_event')
                .then((res) => {
                    this.user = res.data.user
                })
            },
            create_event() {
                this.$router.push('/create_event')
            }
        }
    }
</script>

<style>
    .create {
        padding: 1em 0.5em;
        margin:1em;
        color: white;
        background-color: greenyellow;
    }
</style>