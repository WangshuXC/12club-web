<template>
    <div class="navbar">
        <div class="logo">logo</div>
        <div class="navbar-index">
            <a href="/">首页</a>
            <a href="/anime">动漫</a>
            <a href="/comic">漫画</a>
            <a href="/novel">小说</a>
            <a href="/music">音乐</a>
        </div>
        <input type="text" id='searchText' placeholder="请输入搜索内容" onfocus="this.placeholder=''"
            onblur="this.placeholder='请输入搜索内容'">
        <div class="history">历史</div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            searchText: '',
        }
    },
    methods: {
    }
}
</script>

<style>
.navbar {
    display: flex;
    height: 8vh;
    background-image: linear-gradient(#191825, #ffffff00);
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-around;
    align-items: center;
}

.navbar-index {
    display: flex;
}

.navbar-index a {
    margin-inline: 20px;
}

.navbar input[type="text"] {
    margin-right: 10px;
    padding: 5px;
    border: none;
    outline: none;
    font-size: 16px;
    transition: font-size 0.5s ease;

    background-color: #00000060;
}

a {
    color: #000;
    text-decoration: none;
}
</style>
