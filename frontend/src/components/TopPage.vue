<template>
    <v-row justify="center" align-content="center" class="text-center mb-4">
        <!-- <v-col
        cols="12"
        sm="6">
            <EventList
            v-for="(decided, i) in events"
            :key="i"
            :decided="decided"/>        
        </v-col> -->
        <!-- <v-divider></v-divider> -->
        <v-btn class="mb-4 mx-4 sm-6" height="60px" width="60px" v-on:click="sign_in">
            Sign In
        </v-btn>
        <v-btn class="mb-4 sm-6" height="60px" width="60px" v-on:click="login">
            Login
        </v-btn> 
    </v-row>
</template>

<script>
    import axios from 'axios'
    // import EventList from './EventList'
    
    export default {
        name:'TopPage',
        components:{
            // EventList
        },
        data : () => ({
            events:[]
        }),
        mounted () {
            this.fetchData()
        },
        methods: {
            fetchData() {
                axios.get('/eventlist')
                .then((res) => {
                    this.events = res.data.event
                })
            },
            sign_in() {
                this.$router.push('/sign_in')
            },
            login() {
                this.$router.push('/login')
            },
            all_event() {
                this.$router.push('/all_event')
            }
        }
    }
</script>