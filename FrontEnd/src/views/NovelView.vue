<!-- <template>
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
</style> -->

<template>
    <div class="container">
        <div class="wrapper" :style="{ transform: `translateX(${translateX}px)` }">
            <div class="item" v-for="n in 3" :key="n">Item {{ n }}</div>
        </div>
    </div>
    <button @click="moveTo(0)">Item 1</button>
    <button @click="moveTo(1)">Item 2</button>
    <button @click="moveTo(2)">Item 3</button>
</template>
  

<script>
export default {
    data() {
        return {
            currentIndex: 0, // 当前处于中央的div的索引
            translateX: 0,
        };
    },
    methods: {
        moveTo(index) {
            const itemWidth = window.innerWidth * 0.7; // 单个项的宽度
            const gap = 20; // 项之间的间隔，与CSS中的gap相同
            this.currentIndex = index;
            // 计算偏移量，确保选中的项居中显示
            this.translateX = -(itemWidth + gap) * index + (window.innerWidth - itemWidth) / 2;
        },
    },
    mounted() {
        // 初始化时，让第一个div居中
        this.moveTo(0);
    },
};
</script>

<style scoped>
.container {
    overflow: hidden;
    width: 100vw;
    position: relative;
}

.wrapper {
    display: flex;
    gap: 20px;
    /* 根据需要调整间隔 */
    transition: transform 0.5s ease;
    /* 平滑过渡效果 */
}

.item {
    width: 70vw;
    height: 200px;
    /* 根据需要调整高度 */
    background-color: lightgray;
    /* 仅作为示例 */
}
</style>


