<template>
    <v-carousel height="100vh" width="100vw" show-arrows="hover" cycle interval="3000" hide-delimiter-background
        class="ibanner">
        <v-carousel-item v-for="(item, i) in iBannerList" :key="i" class="sub-div-container">
            <div class="sub-div-background" :style="{ 'background-image': 'url(' + item.background + ')' }">
                <div class="sub-div-info">
                    <h3>{{ item.title }}</h3>
                    <div class="sub-div-info-text">{{ item.info }}</div>
                </div>
            </div>

        </v-carousel-item>
    </v-carousel>
    <div class="container-box">
        <div class="container">
            <label for="title">番剧更新</label>
            <div class="update-box" id="anime">
                <div v-for="(item, index) in animeList" :key="index" class="update-item">
                    <a :href="'/animeplay/' + item.id" class="update-item-url" :alt="item.title">
                        <!-- <div class="update-item-img"
                            :style="item.cover !== 'NULL' ? { 'background-image': `url(${this.DATA_URL}/anime/` + encodeURIComponent(item.title) + '/' + encodeURIComponent(item.cover) + ')' } : { 'background-image': 'url(http://127.0.0.1:3000/anime/Cover.jpg)' }">
                        </div> -->
                        <img class="update-item-img"
                            :src="item.cover !== 'NULL' ? `${this.DATA_URL}/anime/` + encodeURIComponent(item.title) + '/Cover.jpg' : `${this.DATA_URL}/anime/Cover.jpg`">
                    </a>
                    <div class="update-item-title">
                        {{ item.title }}
                    </div>
                </div>
            </div>

            <!-- <label for="title">漫画更新</label>
            <div class="update-box" id="comic">
            </div>

            <label for="title">小说更新</label>
            <div class="update-box" id="novel">
            </div> -->

            <label for="title">音乐更新</label>
            <div class="update-box" id="music">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            iBannerList: [
                { title: 'Item 1', info: '自从连接异次元与当前世界的通道“门”突然出现后已过去十余年，世界上出现了被称为“猎人”的，觉醒了非凡力量的人们。猎人在门内攻略地下城以获取回报以维持生计，但在强者如云的猎人中，「水篠旬」作为被称作人类最弱武器的低级猎人生活着。某一天，遭遇了隐藏在低级地下城中的高级双重地下城后，身受重伤濒临死亡的水篠旬面前出现了神秘的任务窗口。死到临头，决定接受任务的水篠旬，成为了唯一能够「升级」的人——', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/196838.jpg' },
                { title: 'Item 2', info: '自从连接异次元与当前世界的通道“门”突然出现后已过去十余年，世界上出现了被称为“猎人”的，觉醒了非凡力量的人们。猎人在门内攻略地下城以获取回报以维持生计，但在强者如云的猎人中，「水篠旬」作为被称作人类最弱武器的低级猎人生活着。某一天，遭遇了隐藏在低级地下城中的高级双重地下城后，身受重伤濒临死亡的水篠旬面前出现了神秘的任务窗口。死到临头，决定接受任务的水篠旬，成为了唯一能够「升级」的人——', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/268101.jpg' },
                { title: 'Item 3', info: '自从连接异次元与当前世界的通道“门”突然出现后已过去十余年，世界上出现了被称为“猎人”的，觉醒了非凡力量的人们。猎人在门内攻略地下城以获取回报以维持生计，但在强者如云的猎人中，「水篠旬」作为被称作人类最弱武器的低级猎人生活着。某一天，遭遇了隐藏在低级地下城中的高级双重地下城后，身受重伤濒临死亡的水篠旬面前出现了神秘的任务窗口。死到临头，决定接受任务的水篠旬，成为了唯一能够「升级」的人——', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/179540.jpg' },
                { title: 'Item 4', info: 'bvbbbbbbbbbbbbbbb', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/138165.jpg' },
                { title: 'Item 5', info: 'bbbbbbbbbbbbbbbbbb', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/793597.jpg' }
            ],
            animeList: [
                {
                    "id": 15,
                    "title": "小林家的龙女仆",
                    "cover": "Cover.jpg"
                },
                {
                    "id": 14,
                    "title": "紫罗兰永恒花园",
                    "cover": "Cover.jpg"
                },
                {
                    "id": 22,
                    "title": "青春猪头少年不会梦到兔女郎学姐",
                    "cover": "Cover.jpg"
                },
                {
                    "id": 40,
                    "title": "五等分的新娘",
                    "cover": "Cover.jpg"
                },
                {
                    "id": 8,
                    "title": "咒术回战",
                    "cover": "Cover.jpg"
                },
                {
                    "id": 36,
                    "title": "总之就是非常可爱",
                    "cover": "Cover.jpg"
                },
            ],
            prevScrollY: 0,
        }
    },
    mounted() {
        this.setItemsHeight();

        window.addEventListener('scroll', this.handleWheel);
    },
    beforeMount() {
        window.removeEventListener('scroll', this.handleWheel);
    },
    methods: {
        handleWheel() {
            const container = document.querySelector('.container');

            var containerTop = parseInt(getComputedStyle(container).top);
            const screenHeight = window.innerHeight;

            if (window.scrollY == 0) {
                containerTop = screenHeight;
                container.style.top = `${containerTop}px`;
            }

            if (window.scrollY > 0 && window.scrollY < 0.15 * screenHeight) {
                containerTop = screenHeight - window.scrollY;
                container.style.top = `${containerTop}px`;
            }

            if (containerTop > screenHeight) {
                containerTop = screenHeight;
                container.style.top = `${containerTop}px`;
            }

            this.prevScrollY = window.scrollY;
        },
        setItemsHeight() {
            const updateItems = document.querySelectorAll('.update-item-url');
            for (let i = 0; i < updateItems.length; i++) {
                updateItems[i].style.height = `${updateItems[i].offsetWidth * 4 / 3}px`;
            }

            const containerBox = document.querySelector('.container-box');
            const container = document.querySelector('.container');
            containerBox.style.height = `${container.offsetHeight}px`;
        }
    }
}
</script>

<style scoped>
* {
    overflow-x: hidden;
}

body {
    display: flex;
}

.ibanner {

    .sub-div-background {
        width: 100%;
        height: 100%;
        position: relative;
        background-size: cover;
        background-position: center;

        .sub-div-info {
            width: 35vw;
            height: 35vh;
            overflow-y: hidden;
            position: absolute;
            bottom: 16vh;
            left: 5vw;
            padding: 15px;
            border-radius: 15px;
            color: black;
            background-color: #ffffff60;
            box-shadow: 0 12px 15px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);

        }
    }
}

.container-box {
    width: 100vw;
    height: auto;
    overflow-y: hidden;

    .container {
        position: absolute;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        top: calc(100vh - 0px);
        width: 90vw;
        margin-left: 5vw;
        border-radius: 0.5rem;
        background-color: #f3f4f6;
        transition: background-color 0.2s ease-in-out;
        box-shadow: 0 12px 15px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);
        padding: 3vw 0;

        label {
            width: 95%;
            font-size: larger;
            margin-left: 50px;
            margin-bottom: 1rem;
        }

        .update-box {
            display: flex;
            flex-direction: row;
            justify-content: space-between;

            /* background-color: aqua; */
            width: 95%;
            height: auto;

            margin-bottom: 3vw;

            .update-item {
                width: 20%;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                border-radius: 15px;
                transition: background-color 0.2s ease-in-out;

                .update-item-url {
                    width: 90%;
                    overflow: hidden;

                    .update-item-img {
                        width: 100%;
                        border-radius: 10px;
                        background-size: cover;
                    }
                }

                .update-item-title {
                    width: 90%;
                    height: 50px;
                    text-align: start;
                    margin-top: 10px;
                    white-space: pre-wrap;
                    /* overflow: hidden; */
                    /* text-overflow: ellipsis; */
                }
            }
        }

        .update-box#music {
            margin-bottom: 0;
        }
    }
}
</style>
