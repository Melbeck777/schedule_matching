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
                <v-col cols="12">
                    <h2 class="headline font-weight-bold mb-4">Genre</h2>
                    <v-text-field id="form-genre" v-model="genre" outlined required></v-text-field>
                </v-col>
                <v-row>
                    <v-col><h2>Duration</h2></v-col>
                </v-row>
                <v-row>
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
                                class="text-h4"></datepicker></td>
                                <td><h3 class="mb-7 mx-6">～</h3></td>
                                <td><datepicker 
                                :value="this.default2"
                                :format="DatePickerFormat"
                                class="text-h4"></datepicker></td>
                        </tr>
                    </table>
                </v-row>
                <!-- <v-col>
                    <v-row justify="center">
                        <h2 class="headline mx-1 font-weight-bold mb-4">Duration</h2>
                        <h2 class="headline mx-15 font-weight-bold mb-4">Start</h2>
                        <h2 class="headline mx-15 font-weight-bold mb-4">End</h2>
                    </v-row>
                    <v-row justify="center">
                        <datepicker
                        :value="this.default1"
                        :format="DatePickerFormat"
                        height="60px"
                        width="60px"
                        class="text-h4"></datepicker>
                        <h3 class="mb-4 sm-6 mx-6">～</h3>
                        <datepicker 
                        :value="this.default2"
                        :format="DatePickerFormat"
                        class="text-h4"></datepicker>
                    </v-row>
                </v-col> -->
            </v-row>
        </form>
    </v-container>
</template>

<script>
    import Datepicker from 'vuejs-datepicker'

    export default {
        data:()=>({
            default1:'2022-07-14',
            default2:'2022-07-15',
            DatePickerFormat:'yyyy-MM-dd',
            width:'80px',
            height:'80px',
        }),
        components: {
            Datepicker
        },
        methods:{
            resize:function(){
                this.fullheight = window.innerHeight+'px';
            },
        },
        mounted(){
            window.addEventListener('resize',this.resize);
        }
    }
</script>