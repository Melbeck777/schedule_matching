<template>
    <v-container>
        <h1 class="text-center">Create Event</h1>
        <form>
            <v-row class="text-left pt-5">
                <h2 v-show="!isBaseDisplay">Base</h2>
                <button class="show" v-on:click="isBaseDisplay=clickShow(isBaseDisplay)">Show</button>
                <v-col cols="12" v-show="isBaseDisplay">
                    <h2 class="headline font-weight-bold mb-4">Name</h2>
                    <v-text-field id="form-event_name" v-model="name" outlined required></v-text-field>
                </v-col>
                <v-col cols="12" v-show="isBaseDisplay">
                    <h2 class="headline font-weight-bold mb-4">Location</h2>
                    <v-text-field id="form-location" v-model="location" outlined required></v-text-field>
                </v-col>
                <v-col cols="12" v-show="isBaseDisplay">
                    <h2 class="headline font-weight-bold mb-4">Number of times</h2>
                    <v-text-field id="form-num" v-model="num" outlined required></v-text-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <h2>Duration</h2>
                        <button class="show" v-on:click="isDurationDisplay=clickShow(isDurationDisplay)">Show</button>
                    <v-row>
                        <DateInput v-show="isDurationDisplay"></DateInput>
                    </v-row>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <h2 v-show="!isGenreDisplay">Genre</h2>
                    <Genre v-show="isGenreDisplay"></Genre>
                    <button v-on:click="isGenreDisplay=clickShow(isGenreDisplay)" class="show">Show</button>
                </v-col>
            </v-row>
        </form>
    </v-container>
</template>

<script>
    import Genre from './GenreInput.vue'
    import DateInput from './DateInput.vue'
    export default {
        data:()=>({
            default1:'2022-07-14',
            default2:'2022-07-15',
            DatePickerFormat:'yyyy-MM-dd',
            genres:[{name:''}],
            categories:[{name:''}],
            isGenreDisplay:true,
            isDurationDisplay:true,
            isBaseDisplay:true
        }),
        components:{
            Genre,
            DateInput
        },
        methods:{
            clickShow: function(buttonName){
                console.log(buttonName);
                console.log(!buttonName);
                return !buttonName;
            },
        }
    }
</script>

<style>
    .duration {
        padding:1em;
        margin:1em;
    }
    .show{
        padding:1em;
        margin:1em;
        background-color:lightblue;
        color:white;
    }
</style>