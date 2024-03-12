<template>
    <div class="admin-login">
        <h1>Admin Login</h1>
        <br>
        <v-form v-model="form" @submit.prevent="login">
            <v-text-field v-model="username" :readonly="loading" :rules="[usernameRequired]" label="Username"
                clearable></v-text-field>

            <v-text-field v-model="password" :readonly="loading" :rules="[passwordRequired]" label="Password"
                :append-inner-icon="show ? 'mdi-eye' : 'mdi-eye-off'" @click:append-inner="show = !show"
                :type="show ? 'text' : 'password'" placeholder="Enter your password"></v-text-field>

            <br>

            <v-btn :disabled="!form" :loading="loading" color="success" size="large" type="submit" variant="elevated"
                block>
                Log in
            </v-btn>
        </v-form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            form: false,
            loading: false,
            show: false,
            username: '',
            password: null
        };
    },
    mounted() {

    },
    methods: {
        usernameRequired(v) {
            return !!v || '用户名为空'
        },
        passwordRequired(v) {
            return !!v || '密码为空'
        },
        login() {
            if (!this.form) return;
            this.loading = true;

            const formData = {
                username: this.username,
                password: this.password
            };
            axios.post(`${this.API_URL}/login`, formData, { withCredentials: true })
                .then(response => {
                    setTimeout(() => (this.loading = false), 1000)
                    this.$router.push('/admin/op');
                    console.log(response);
                })
                .catch(error => {
                    // 处理错误逻辑
                    console.error(error);
                });
        },
        signup() {
            console.log('signup')
            const formData = {
                username: this.username,
                password: this.password
            };
            axios.post(`${this.API_URL}/signup`, formData)
                .then(response => {
                    // 登录成功逻辑
                    console.log(response);
                })
                .catch(error => {
                    // 处理错误逻辑
                    console.error(error);
                });
        }
    }
};
</script>

<style scoped>
.admin-login {
    max-width: 30vw;
    margin-inline: auto;
    margin-top: calc(50vh - 200px);
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
}

button {
    background-color: #007bff;
    color: white;
    padding: 8px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
</style>
