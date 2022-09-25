<template>
    <div>
        <div class="text-body-1 ml-4 my-2">
            {{decided.date}}
        </div>
        <v-divider></v-divider>
        <EventShow
        v-for="(event,i) in decided.data"
        :key="i"
        :event="event"/>
    </div>
</template>

<script>
    import EventShow from './EventShow.vue'
    export default {
        name:'EventList',
        components:{
            EventShow,
        },
        props:['decided'],
        data: () => ({
            show:false
        })
    }
</script>