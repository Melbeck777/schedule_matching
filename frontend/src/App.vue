<template>
  <v-app>
    <v-card class="green"></v-card>
    
    <center>
      <div class="header">
        <v-img
          alt="SM Logo"
          align="center"
          class=""
          contain
          src="./assets/Logo2_cat.jpeg"
          width="300"
        />
        <h1 class="mb-5">Schedule Matching</h1>
      </div>
    </center>
    <v-card>
      <router-view class="mt-n3"/>
    </v-card>
    
  </v-app>
</template>

<script>

export default {
  name: 'App',
  components: {
},

  data: () => ({
    //
  }),
};
</script>
