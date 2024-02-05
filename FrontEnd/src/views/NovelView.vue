<template>
    <div class="anime-container">
        <div class="sort-bar"></div>
        <div class="bangumi-list">
            <div v-for="(item, index) in bangumiList" :key="index" class="bangumi-box">
                <div class="bangumi-img" :style="{ 'background-image': 'url(' + item.img + ')' }">

                </div>
                <div class="bangumi-info">
                    {{ item.name }}
                </div>
            </div>
        </div>
        <v-pagination v-model="page" :length="pageNum" :total-visible="5" prev-icon="mdi-chevron-left"
            next-icon="mdi-chevron-right" class="page-control"></v-pagination>
    </div>
</template>

<script>
export default {
    data() {
        return {
            page: 4,
            pageNum: 10,
            bangumiList: [
                {
                    img: 'https://cdn.yinghuacdn.top/upload/vod/20240120-1/4ff041d9f3d139ba30addc29b73361e9.jpg',
                    url: '/animeplay',
                    name: '福利连'
                },
                {
                    img: 'https://cdn.yinghuacdn.top/upload/vod/20240120-1/4ff041d9f3d139ba30addc29b73361e9.jpg',
                    url: '/animeplay',
                    name: '福利连2'
                },
                {
                    img: 'https://cdn.yinghuacdn.top/upload/vod/20240120-1/4ff041d9f3d139ba30addc29b73361e9.jpg',
                    url: '/animeplay',
                    name: '福利连3'
                },
                {
                    img: 'https://cdn.yinghuacdn.top/upload/vod/20240120-1/4ff041d9f3d139ba30addc29b73361e9.jpg',
                    url: '/animeplay',
                    name: '福利连4'
                },
                {
                    img: 'https://cdn.yinghuacdn.top/upload/vod/20240120-1/4ff041d9f3d139ba30addc29b73361e9.jpg',
                    url: '/animeplay',
                    name: '福利连5'
                },
                {
                    img: 'https://cdn.yinghuacdn.top/upload/vod/20240120-1/4ff041d9f3d139ba30addc29b73361e9.jpg',
                    url: '/animeplay',
                    name: '福利连6'
                },
                {
                    img: 'https://cdn.yinghuacdn.top/upload/vod/20240120-1/4ff041d9f3d139ba30addc29b73361e9.jpg',
                    url: '/animeplay',
                    name: '福利连7'
                },
            ],
        }
    },
    methods: {
    }
}
</script>

<style>
.anime-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    min-height: 90vh;
    margin-top: 10vh;
    /* background-color: black; */

    .sort-bar {
        width: 90%;
        height: 5vh;
        background-color: aqua;
    }

    .bangumi-list {
        display: flex;
        width: 90%;
        min-height: 80vh;
        flex-wrap: wrap;
        background-color: rgb(200, 255, 0);

        .bangumi-box {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-top: 15px;
            width: 25%;
            height: calc(22.5vw*4/3);
            /* background-color: blue; */


            .bangumi-img {
                width: 90%;
                height: 90%;
                border-radius: 10px;
                background-size: cover;
            }

            .bangumi-info {
                width: 90%;
                height: calc(10%-10px);
                text-align: center;
                margin-top: 10px;
            }
        }
    }

    .page-control {
        margin-top: 3%;
    }
}
</style>
