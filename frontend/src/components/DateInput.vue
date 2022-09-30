<template>
    <v-row>
        <v-col>
            <h2>Start Date</h2>
            <v-date-picker v-model="startDate"></v-date-picker>
        </v-col>        
        <v-col>
            <h2>End Date</h2>
            <v-date-picker v-model="endDate"></v-date-picker>
        </v-col>        
    </v-row>
</template>