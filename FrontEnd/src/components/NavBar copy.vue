<template>
    <el-menu :default-active="getCurrentMenuUrl()" class="el-menu" mode="horizontal" router="false" menu-trigger="hover"
        :ellipsis="false" unique-opened>
        <el-menu-item index="/">首页</el-menu-item>

        <el-input v-model="searchText" class="search" size="large" placeholder="输入关键字进行搜索..." />

        <el-menu-item index="/anime">动漫</el-menu-item>
        <el-menu-item index="/comic">漫画</el-menu-item>
        <el-menu-item index="/novel">小说</el-menu-item>
        <el-sub-menu index="about">
            <template #title>关于</template>
            <el-menu-item index="/about">网站简介</el-menu-item>

            <el-popover placement="bottom" :width="200" trigger="hover">
                <template #reference>
                    <el-menu-item>加入我们</el-menu-item>
                </template>
                <p>QQ群：973304356</p>
                <el-image style="width: 100%; height: 100%" :src="imageUrl" :fit="contain" />
            </el-popover>
        </el-sub-menu>
    </el-menu>
</template>

<script>
import qqImage from '@/assets/imgs/qq.jpg'
export default {
    data() {
        return {
            searchText: '',
            imageUrl: qqImage
        }
    },
    methods: {
        getCurrentMenuUrl() {
            return this.$route.path
        }
    }
}
</script>

<style>
.flex-grow {
    flex-grow: 1;
}

.search {
    max-width: 50%;
    min-width: 35%;
    margin-left: 20%;
    margin-right: 10%;
    margin-bottom: 10px;
}
</style>
