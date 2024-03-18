<template>
    <div class="anime-container">
        <div class="sort-bar">
            <div class="sort-bar-item" :class="{ on: sort == 0 }" id="0" @click="updateSort(0)">
                <font-awesome-icon :icon="['fas', 'caret-up']" class="up" :class="{ active: isAsc }" />
                <span>播放数量</span>
                <font-awesome-icon :icon="['fas', 'caret-down']" class="down" :class="{ active: !isAsc }" />
            </div>
            <div class="sort-bar-item" :class="{ on: sort == 1 }" id="1" @click="updateSort(1)">
                <font-awesome-icon :icon="['fas', 'caret-up']" class="up" :class="{ active: isAsc }" />
                <span>下载数量</span>
                <font-awesome-icon :icon="['fas', 'caret-down']" class="down" :class="{ active: !isAsc }" />
            </div>
            <div class="sort-bar-item" :class="{ on: sort == 2 }" id="2" @click="updateSort(2)">
                <font-awesome-icon :icon="['fas', 'caret-up']" class="up" :class="{ active: isAsc }" />
                <span>更新时间</span>
                <font-awesome-icon :icon="['fas', 'caret-down']" class="down" :class="{ active: !isAsc }" />
            </div>
        </div>
        <div class="bangumi-list">
            <div v-for="(item, index) in bangumiList" :key="index" class="bangumi-box">
                <a :href="'/animeplay/' + item.id" class="bangumi-url" :alt="item.title">
                    <!-- <div class="bangumi-img"
                        :style="item.cover !== 'NULL' ? { 'background-image': `url(${this.DATA_URL}/anime/` + encodeURIComponent(item.title) + '/Cover.jpg' + ')' } : { 'background-image': 'url(http://127.0.0.1:3000/anime/Cover.jpg)' }">
                    </div> -->
                    <img class="bangumi-img"
                        :src="item.cover !== 'NULL' ? `${this.DATA_URL}/anime/` + encodeURIComponent(item.title) + '/Cover.jpg' : `${this.DATA_URL}/anime/Cover.jpg`">
                </a>
                <div class="bangumi-info">
                    {{ item.title }}
                </div>
            </div>
        </div>
        <v-pagination v-model="page" :length="pageNum" :total-visible="5" prev-icon="mdi-chevron-left"
            next-icon="mdi-chevron-right" class="page-control" color="#00a1d6"></v-pagination>
        <div class="white"></div>
    </div>
</template>

<script>
import axios from 'axios';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faCaretUp, faCaretDown } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faCaretUp, faCaretDown)

export default {
    data() {
        return {
            page: 1,
            pageNum: 1,
            bangumiList: [],
            sort: 0,
            isAsc: false,
        }
    },
    components: {
        FontAwesomeIcon,
    },
    beforeMount() {
        this.loadBangumiData();
    },
    mounted() {
        if (this.bangumiList.length === 0) {
            this.loadBangumiData();
        }
    },
    watch: {
        page() {
            this.loadBangumiData();
            this.scrollToTop();
        }
    },
    methods: {
        loadBangumiData() {
            const sortFields = ['view_count', 'download_count', 'update_time'];
            let sortParam = sortFields[this.sort] || 'id';
            let orderbyParam = this.isAsc ? 'asc' : 'desc';

            let requestUrl = `${this.API_URL}/animepage/${this.page}?sort=${sortParam}&orderby=${orderbyParam}`;
            axios.get(requestUrl)
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
        },
        updateSort(id) {
            if (this.sort === id) {
                this.isAsc = !this.isAsc;
            } else {
                this.sort = id;
                this.isAsc = false;
            }
            this.loadBangumiData();
            this.page = 1;
        },
    },
}
</script>

<style>
.anime-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    margin-top: 10vh;
    /* background-color: black; */

    .sort-bar {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 2px;
        width: 88%;
        height: 5vh;
        user-select: none;
        /* background-color: aqua; */

        .sort-bar-item {
            min-width: 6.5%;
            margin-right: 5%;
            position: relative;
            cursor: pointer;

            .up {
                position: absolute;
                top: 0;
                right: 0;
                color: #dddddd;
            }



            .down {
                position: absolute;
                bottom: 0;
                right: 0;
                color: #dddddd;
            }
        }

        .sort-bar-item.on {
            color: #00a1d6;

            .up.active {
                color: #00a1d6;
            }

            .down.active {
                color: #00a1d6
            }
        }
    }

    .bangumi-list {
        display: flex;
        width: 90%;
        min-height: 20vh;
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

            border-radius: 15px;
            transition: background-color 0.2s ease-in-out;


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

        .bangumi-box:hover {
            background-color: #e0f3fa;
        }
    }

    .page-control {
        margin-top: 3%;
    }

    .white {
        width: 100%;
        height: 10vh;
    }
}
</style>
