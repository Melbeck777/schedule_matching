<template>
    <v-container>
        <h1 class="text-center">Create Event</h1>
        <form>
            <v-row class="text-left pt-5">
                <v-col cols="12">
                    <h2 class="headline font-weight-bold mb-4">Name</h2>
                    <v-text-field id="form-event_name" v-model="name" outlined required></v-text-field>
                </v-col>
                <v-col cols="12">
                    <h2 class="headline font-weight-bold mb-4">Location</h2>
                    <v-text-field id="form-location" v-model="location" outlined required></v-text-field>
                </v-col>
                <v-col cols="12">
                    <h2 class="headline font-weight-bold mb-4">Number of times</h2>
                    <v-text-field id="form-num" v-model="num" outlined required></v-text-field>
                </v-col>
                <v-row>
                    <h2>Duration</h2>
                    <table>
                        <tr class="text-left">
                            <td><h2>Start</h2></td>
                            <td></td>
                            <td><h2>End</h2></td>
                        </tr>
                        <tr>
                            <td><datepicker
                                :value="this.default1"
                                :format="DatePickerFormat"
                                height="60px"
                                width="60px"
                                class="text-h4"
                                color="primary"></datepicker></td>
                                <td><h3 class="mb-7 mx-6">～</h3></td>
                                <td><datepicker 
                                :value="this.default2"
                                :format="DatePickerFormat"
                                class="text-h4"></datepicker></td>
                        </tr>
                    </table>
                </v-row>
                <v-col>
                    <Genre></Genre>
                </v-col>
            </v-row>
        </form>
    </v-container>
</template>

<script>
    import Datepicker from 'vuejs-datepicker'
    import Genre from './GenreInput.vue'
    export default {
        data:()=>({
            default1:'2022-07-14',
            default2:'2022-07-15',
            DatePickerFormat:'yyyy-MM-dd',
            width:'80px',
            height:'80px',
            genres:[{name:''}],
            categories:[{name:''}]
        }),
        components: {
        Datepicker,
        Genre,
        },
        methods:{
            resize:function(){
                this.fullheight = window.innerHeight+'px';
            },
            add_genre: function(){
                this.genre.push({name:''})
            },
            del_genre: function(index){
                this.genre.slice(index,1)
            },
            add_category: function(){
                this.category.push({name:''})
            },
            del_category:function(index) {
                this.genre.slice(index,1)
            }
        },
        mounted(){
            window.addEventListener('resize',this.resize);
        }
    }
</script>