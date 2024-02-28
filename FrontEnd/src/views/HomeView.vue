<template>
    <div class="ibanner" ref="ibanner">
        <div class="sub-div-container">
            <div v-for="(item, index) in iBannerList" :key="index" class="sub-div"
                :style="{ backgroundImage: `url(${item.background})` }">
                {{ item.text }}
            </div>
        </div>
    </div>
    <div class="container-box">
        <div class="container">
            <label for="title">番剧更新</label>
            <div class="update-box" id="anime">
                <div v-for="(item, index) in animeList" :key="index" class="update-item">
                    <a :href="'/animeplay/' + item.id" class="update-item-url" :alt="item.title">
                        <div class="update-item-img"
                            :style="item.cover !== 'NULL' ? { 'background-image': `url(${this.DATA_URL}/anime/` + encodeURIComponent(item.title) + '/' + encodeURIComponent(item.cover) + ')' } : { 'background-image': 'url(http://127.0.0.1:3000/anime/Cover.jpg)' }">
                        </div>
                    </a>
                    <div class="update-item-title">
                        {{ item.title }}
                    </div>
                </div>
            </div>

            <label for="title">漫画更新</label>
            <div class="update-box" id="comic">
            </div>

            <label for="title">小说更新</label>
            <div class="update-box" id="novel">
            </div>

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
                { text: 'Item 1', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/196838.jpg' },
                { text: 'Item 2', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/268101.jpg' },
                { text: 'Item 3', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/179540.jpg' },
                { text: 'Item 4', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/138165.jpg' },
                { text: 'Item 5', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/793597.jpg' }
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
        const ibanner = this.$refs.ibanner;
        const subDivContainer = ibanner.querySelector('.sub-div-container');
        const ibannerWidth = ibanner.offsetWidth;

        subDivContainer.style.width = `${ibannerWidth * this.iBannerList.length}px`;

        const animate = () => {
            setTimeout(() => {
                subDivContainer.style.transform = `translateX(-${ibannerWidth}px)`;
                setTimeout(() => {
                    subDivContainer.style.transition = 'transform 0s';
                    this.iBannerList.push(this.iBannerList.shift());
                    subDivContainer.style.transform = '';
                    animate();
                }, 1000);
                subDivContainer.style.transition = 'transform 0.5s ease-out';
            }, 2000);
        };

        this.setItemsHeight();
        animate();
        window.addEventListener('scroll', this.handleWheel);
    },
    beforeMount() {
        window.removeEventListener('scroll', this.handleWheel);
    },
    methods: {
        handleWheel() {
            console.log(this.prevScrollY);
            const container = document.querySelector('.container');
            var containerTop = parseInt(getComputedStyle(container).top);
            const screenHeight = window.innerHeight;

            if (window.scrollY == 0) {
                containerTop = screenHeight;
                container.style.top = `${containerTop}px`;
            }

            if (window.scrollY > 0 && window.scrollY < 0.15 * screenHeight) {
                containerTop = screenHeight - window.scrollY
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

<style>
* {
    overflow-x: hidden;
}

body {
    display: flex;
}

.ibanner {
    width: 100vw;
    height: 100vh;
    position: relative;
    overflow: hidden;

    .sub-div-container {
        display: flex;
        width: 100%;
        height: 100%;
        overflow: hidden;
        transition: transform 0.5s ease;

        .sub-div {
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            color: #ffffff;
            text-align: center;
            font-size: 54px;
            line-height: 100vh;
            background-size: cover;
            background-position: center center;
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
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                border-radius: 15px;
                transition: background-color 0.2s ease-in-out;

                .update-item-url {
                    width: 90%;
                    height: 90%;

                    .update-item-img {
                        width: 100%;
                        height: 100%;
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
