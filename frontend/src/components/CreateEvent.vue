<template>
    <v-container>
        <h1 class="text-center">Create Event</h1>
        <form v-on:click="to_genre">
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
            <v-col cols="12" class="text-center">
                <v-btn
                color="green"
                absolute
                center
                fab
                middle
                class="mt-4 mb-8"
                type="submit">
                <v-icon>mdi-cat</v-icon>
            </v-btn>
            </v-col>
        </form>
    </v-container>
</template>

<script>
    import DateInput from './DateInput.vue'
    export default {
        data:()=>({
            default1:'2022-07-14',
            default2:'2022-07-15',
            DatePickerFormat:'yyyy-MM-dd',
            genres:[{name:'',
            categories:[]}],
            isGenreDisplay:true,
            isDurationDisplay:true,
            isBaseDisplay:true
        }),
        components:{
            DateInput
        },
        methods:{
            clickShow: function(buttonName){
                return !buttonName;
            },
            to_genre(){
                this.$router.push('/add_genre')
            }
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