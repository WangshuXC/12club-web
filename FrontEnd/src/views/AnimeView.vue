<template>
    <div class="anime-container">
        <div class="sort-bar"></div>
        <div class="bangumi-list">
            <div v-for="(item, index) in bangumiList" :key="index" class="bangumi-box">
                <a :href="'/animeplay/' + item.id" class="bangumi-url" :alt="item.title">
                    <div class="bangumi-img"
                        :style="item.cover !== 'NULL' ? { 'background-image': 'url(http://127.0.0.1:3000/anime/' + encodeURIComponent(item.title) + '/' + encodeURIComponent(item.cover) + ')' } : { 'background-image': 'url(http://127.0.0.1:3000/anime/Cover.jpg)' }">
                    </div>
                </a>
                <div class="bangumi-info">
                    {{ item.title }}
                </div>
            </div>
        </div>
        <v-pagination v-model="page" :length="pageNum" :total-visible="5" prev-icon="mdi-chevron-left"
            next-icon="mdi-chevron-right" class="page-control"></v-pagination>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            page: 1,
            pageNum: 1,
            bangumiList: [
            ],
        }
    },
    methods: {
        loadBangumiData() {
            axios.get(`http://127.0.0.1:5000/api/animepage/${this.page}`)
                .then(response => {
                    this.pageNum = response.data.total_page;
                    this.bangumiList = response.data.results;
                })
                .catch(error => {
                    console.error("There was an error fetching the anime data:", error);
                });
        },
        scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    },
    mounted() {
        this.loadBangumiData();
    },
    watch: {
        page() {
            this.loadBangumiData();
            this.scrollToTop();
        }
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
        margin-left: 2.25%;
        background-color: aqua;
    }

    .bangumi-list {
        display: flex;
        width: 90%;
        min-height: 80vh;
        flex-wrap: wrap;
        /* background-color: rgb(200, 255, 0); */

        .bangumi-box {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-top: 15px;
            width: 25%;
            height: calc(22.5vw*4/3);
            /* background-color: blue; */


            .bangumi-url {
                width: 90%;
                height: 90%;

                .bangumi-img {
                    width: 100%;
                    height: 100%;
                    border-radius: 10px;
                    background-size: cover;
                }
            }

            .bangumi-info {
                width: 90%;
                height: calc(10%-10px);
                text-align: center;
                margin-top: 10px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }
        }
    }

    .page-control {
        margin-top: 3%;
    }
}
</style>
