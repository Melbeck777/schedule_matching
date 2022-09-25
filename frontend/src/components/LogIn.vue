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
                        Password
                    </h2>
                    <v-text-field id="form-password" v-model="password" outlined required></v-text-field>
                </v-col>
            </v-row>
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
        </form>
    </v-container>
</template>

<script>
    import axios from 'axios';

    export default {
        data:() => ({
            user_data:{
                email:'',
                password:'',
            },
        }),
        mounted(){
            this.verify();
        },
        methods:{
            send: function(){
                let user_data = {email:this.email, password:this.password};
                console.log(user_data);
                axios.post('/login',user_data)
                    .then(res => {
                        console.log(res);
                        this.$router.push('/');
                    })
                    .catch(err => {console.log(err)})
            },
            verify(){
                // axios.get('https:///127.0.0.1:5000/login/verify')
                // .then((res) => {
                //     this.flag = res.data.flag;
                //     this.user_id = res.data.user_id;
                // })
            },
            home(){
                this.$router.push('/')
            }
        }
    }
</script>