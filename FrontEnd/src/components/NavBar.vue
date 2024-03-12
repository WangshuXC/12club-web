<template>
    <div class="navbar">
        <div class="logo">logo.jpg</div>
        <div class="navbar-index">
            <a href="/">首页</a>
            <a href="/anime">动漫</a>
            <!-- <a href="/comic">漫画</a>
            <a href="/novel">小说</a> -->
            <a href="/music">音乐</a>
        </div>
        <div class="search-box">
            <input class="input-box" type="text" v-model='searchText' placeholder="请输入搜索内容"
                onfocus="this.placeholder=''" onblur="this.placeholder='请输入搜索内容'">
            <font-awesome-icon :icon="['fas', 'magnifying-glass']" class="search-btn" />
        </div>

        <div class="history">历史</div>
    </div>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faMagnifyingGlass)

export default {
    data() {
        return {
            searchText: '',
        }
    },
    components: {
        FontAwesomeIcon,
    },
    methods: {
    }
}
</script>

<style>
.navbar {
    display: flex;
    height: 8vh;
    background-image: linear-gradient(#f2faff9a, #ffffff00);
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-around;
    align-items: center;
    color: #000000;
    user-select: none;
    overflow-y: hidden;
}

.navbar-index {
    display: flex;
}

.navbar-index a {
    margin-inline: 20px;
}

.navbar .search-box {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: auto;
    height: auto;
    border-radius: 10px;
    padding: 2px;
    background-color: #0000002d;
}

.search-btn {
    margin-right: 5px;
    color: #0000006a;
}

.navbar input[type="text"] {
    margin-right: 10px;
    padding: 5px;
    border: none;
    outline: none;
    font-size: 16px;
    transition: font-size 0.5s ease;

    background-color: transparent;
}

a {
    color: #000000;
    text-decoration: none;
}
</style>
