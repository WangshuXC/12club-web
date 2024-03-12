<template>
    <div class="admin-login">
        <h1>Admin Login</h1>
        <form>
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" placeholder="Enter your username" required>

            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" placeholder="Enter your password" required>

            <button type="login" @click="login()">Login</button>
            <button type="signup" @click="signup()">Signup</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login() {
            const formData = {
                username: this.username,
                password: this.password
            };
            axios.post(`${this.API_URL}/login`, formData)
                .then(response => {
                    // 登录成功逻辑
                    console.log(response.data);
                })
                .catch(error => {
                    // 处理错误逻辑
                    console.error(error);
                });
            console.log('Username:', this.username);
            console.log('Password:', this.password);
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
                    console.log(response.data);
                })
                .catch(error => {
                    // 处理错误逻辑
                    console.error(error);
                });
            console.log('Username:', this.username);
            console.log('Password:', this.password);
        }
    }
};
</script>

<style scoped>
.admin-login {
    max-width: 300px;
    margin: 0 auto;
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
