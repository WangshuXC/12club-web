<template>
    <div class="admin-login">
        <h1>Admin Login</h1>
        <form @submit.prevent="login">
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" placeholder="Enter your username" required>

            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" placeholder="Enter your password" required>

            <button type="submit">Login</button>
        </form>
    </div>
</template>

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

<script>
export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login() {
            // 在这里编写登录逻辑，可以通过 this.username 和 this.password 获取输入的用户名和密码
            // 进行登录验证，例如提交表单至后端进行验证
            console.log('Username:', this.username);
            console.log('Password:', this.password);
        }
    }
};
</script>