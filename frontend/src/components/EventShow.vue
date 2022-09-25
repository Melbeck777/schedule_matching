<template>
    <div>
        <v-row align-content="center">
            <v-col class="font-weight-black text-h6 ml-12 ma-2 cols=4">
                {{event.event_name}}
            </v-col>
            <v-col class="mt-3">
                <v-icon>mdi-close</v-icon>
            </v-col>
            <v-col class="text-h6 ma-2">
                {{event.location}}
            </v-col>
            <v-col>
                <v-btn
                icon
                @click="show = !show"
                class="my-1">
                <v-icon>{{show ? 'mdi-chevron-up':'mdi-chevron-down'}}</v-icon>
                </v-btn>
            </v-col>
        </v-row>
        <v-expand-transition>
            <div v-show="show">
                <v-divider></v-divider>
                <v-card color="grey lighten-3" elevation="0">
                    <center>
                        <v-btn
                        dark
                        color="yellow"
                        class="ma-2"
                        v-on:click="$emit('edit')">
                        Edit</v-btn>
                        <v-btn
                        dark
                        color="green"
                        class="ma-2"
                        v-on:click="$emit('show')">
                        Show</v-btn>
                    </center>
                </v-card>
            </div>
        </v-expand-transition>
    </div>
</template>

<script>
    export default{
        name:'EventShow',
        components:{
        },
        props:['event'],
        data: () => ({
            show:false,
        }),
        methods:{            
        }
    }
</script>