<template>
    <v-container>
        <form v-on:submit.prevent="send">
            <v-row class="text-left pt-5">
                <v-col cols="12">
                    <h2 class="headline font-weight-bold mb-3">
                        Email
                    </h2>
                    <v-text-field id="form-email" v-model="email" outlined required></v-text-field>
                </v-col>
                <v-col cols="12">
                    <h2 class="headline font-weight-bold mb-3">
                        Name
                    </h2>
                    <v-text-field id="form-name" v-model="name" outlined required></v-text-field>
                </v-col>
                <v-col cols="12">
                    <h2 class="headline font-weight-bold mb-3">
                        Password
                    </h2>
                    <v-text-field id="form-password" v-model="password" outlined required></v-text-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" class="text-center">
                    <v-btn color="green" 
                    dark
                    absolute
                    center
                    fab
                    middle
                    bottom
                    class="mt-4 mb-8"
                    type="submit">
                        <v-icon>mdi-cat</v-icon>
                    </v-btn>
                </v-col>
            </v-row>
        </form>
        
    </v-container>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'SignIn',
        data:() => ({
            user_data:{name:'',email:'',password:''},
        }),
        methods:{
            send: function() {
                let user_data = {email:this.email, name:this.name, password:this.password};
                // user_data.append("email",this.email);
                // user_data.append("name",this.name);
                // user_data.append("password",this.password);
                // console.log(this.email);
                // console.log(this.name);
                // console.log(this.password);
                console.log(user_data);
                axios.post("/signup",user_data)
                    .then(res => {
                        console.log(res);
                        this.$router.push('/');
                    })
                    .catch(err => {console.log(err)})
            },
            new_sign(id) {
                this.$router.push('/'+id);
            },
            home(){
                this.$router.push('/');
            }
        }
    }
</script>