<template>
    <div class="animeplay-container">
        <div class="video-player">
            <video id="player" playsinline controls>
                <source :src="videoUrl">
            </video>
        </div>
        <div class="right-box-container">
            <div class="right-box" id="play">
                <div class="right-box-title">
                    <div class="left">
                        正片
                        <span>({{ currentEpisode }}/{{ episode }})</span>
                    </div>
                    <div class="right"></div>
                </div>

                <div class="number-list">
                    <div v-for="(item, index) in episodeNameList" :key="index" class="number-list-item"
                        :class="{ current: index == currentEpisode }">
                        {{ item }}
                    </div>
                </div>
            </div>

            <div class="right-box" id="download">
                <div class="right-box-title">
                    <div class="left">下载</div>
                    <div class="right"></div>
                </div>

                <div class="number-list" @mousedown="handleMouseDown">
                    <div v-for="(item, index) in episodeNameList" :key="index" class="number-list-item"
                        :class="{ 'current': downloadedIndex.includes(index) }" @click="Download(index)"
                        @mousemove="handleMouseMove(index)" @mouseup="handleMouseUp">
                        {{ item }}
                    </div>
                </div>
            </div>
        </div>
        <div class="left-box-container">
            <div class="media-info">
                <img src="http://127.0.0.1:3000/anime/药屋少女的呢喃/Cover.jpg" alt="" class="cover">
                <div class="info">
                    <p class="title">药屋少女的呢喃</p>
                    <p class="text">{{ view_count }}播放&nbsp; &nbsp;·&nbsp;&nbsp;{{ download_count }}下载</p>
                    <p class="text">{{ isOver ? "已完结，全" + this.episode + "话" : "连载中，最近更新时间：" + update_date }}</p>
                    <p class="introduction" :class="{ expand: isExpand }" ref="introductionRef">
                        简介：
                        {{ description }}
                    </p>
                    <div v-if="isNeedExpand && isExpand" class="reduce" @click="reduce">收起</div>
                    <div v-if="isNeedExpand && !isExpand" class="gradient" @click="expend">
                        <div class="expandBtn">展开</div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import Plyr from 'plyr';
import 'plyr/dist/plyr.css';

export default {
    data() {
        return {
            videoUrl: 'http://127.0.0.1:3000/anime/药屋少女的呢喃/1.mp4',
            episode: 10,
            currentEpisode: 2,
            episodeNameList: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            downloadedIndex: [],
            dragging: false,
            isOver: false,
            isExpand: false,
            isNeedExpand: false,
            update_date: "2024-02-06 15:22:38",
            view_count: 6666,
            download_count: 666,
            description: `寿命逾千年的魔法使芙莉莲，以曾经共同战胜魔王的勇者辛美尔之死为契机，踏上了了解人类的旅途。
            
            邂逅了同属勇者小队的僧侣海塔与战士艾泽分别培养出的菲伦与休塔尔克，芙莉莲与二人一同前往灵魂安眠之地。为了前去需要【一级魔法使】资格，因此芙莉莲与菲伦前往魔法都市维萨斯特，参加一级魔法使选拔测验。在那里有着形形色色的卓越魔法使…此刻，最顶尖的魔法将在维萨斯特展开激烈碰撞！
            邂逅了同属勇者小队的僧侣海塔与战士艾泽分别培养出的菲伦与休塔尔克，芙莉莲与二人一同前往灵魂安眠之地。为了前去需要【一级魔法使】资格，因此芙莉莲与菲伦前往魔法都市维萨斯特，参加一级魔法使选拔测验。在那里有着形形色色的卓越魔法使…此刻，最顶尖的魔法将在维萨斯特展开激烈碰撞！
            邂逅了同属勇者小队的僧侣海塔与战士艾泽分别培养出的菲伦与休
            邂逅了同属勇者小队的僧侣海塔与战士艾泽分别培养出的菲伦与休
            邂逅了同属勇者小队的僧侣海塔与战士艾泽分别培养出的菲伦与休
            `
        };
    },
    mounted() {
        this.initPlayer();
        this.$nextTick(() => {
            var introduction = this.$refs.introductionRef;
            if (introduction.scrollHeight > introduction.clientHeight) {
                this.isNeedExpand = true;
            } else {
                this.isNeedExpand = false;
            }
        });
    },
    methods: {
        initPlayer() {
            this.player = new Plyr('#player', {
                controls: ['play-large', 'play', 'progress', 'current-time', 'mute', 'volume', 'settings', 'download', 'fullscreen'],
                speed: { selected: 1, options: [0.5, 0.75, 1, 1.25, 1.5, 2] },
            });
        },
        Download(index) {
            if (this.downloadedIndex.includes(index)) {
                // this.downloadedIndex = this.downloadedIndex.filter(i => i !== index);
            } else {
                this.downloadedIndex.push(index);
            }
        },
        handleMouseDown() {
            this.dragging = true;
        },
        handleMouseMove(index) {
            if (this.dragging && !this.downloadedIndex.includes(index)) {
                this.downloadedIndex.push(index);
            }
        },
        handleMouseUp() {
            this.dragging = false;
        },
        expend() {
            this.isExpand = true;
            const infoElement = document.querySelector('.info');
            if (infoElement) {
                infoElement.style.maxHeight = '100vh';
            }
        },
        reduce() {
            this.isExpand = false;
            const infoElement = document.querySelector('.info');
            if (infoElement) {
                infoElement.style.maxHeight = 'calc(68vw*.25)';
            }
        }
    },
};
</script>

<style>
.animeplay-container {
    margin-top: 10vh;
    width: 95vw;
    margin-left: 2.5vw;
    min-height: 90vh;

    position: relative;

    .video-player {
        width: 68vw;
        height: calc(68vw*.5625);
        display: flex;
        margin-right: 2vw;

        position: absolute;
        left: 0;
        top: 0;
    }

    .right-box-container {
        width: 25vw;
        display: flex;
        flex-direction: column;

        position: absolute;
        right: 0;
        top: 0;
    }

    .left-box-container {
        width: 68vw;
        min-height: 60vh;
        display: flex;
        flex-direction: column;

        /* background-color: #61666d; */

        position: absolute;
        left: 0;
        top: calc(68vw*.5625 + 5vh);
    }
}

.left-box-container {
    .media-info {
        width: 100%;
        /* max-height: calc(68vw*.25); */
        display: flex;
        justify-content: space-between;

        .cover {
            height: calc(68vw*.25);
            width: calc(68vw*.1875);
            border-radius: 6px;
        }

        .info {
            display: flex;
            flex-direction: column;
            padding-left: 10px;
            width: 80%;
            max-height: calc(68vw*.25);

            position: relative;

            .title {
                height: 25px;
                font-size: 18px;
                margin-bottom: 10px;
                font-weight: 550;
            }

            .text {
                height: 18px;
                font-size: 14px;
                margin-bottom: 6px;
                color: #61666d;
            }

            .introduction {
                font-size: 14px;
                white-space: pre-line;
                overflow: hidden;
                text-overflow: ellipsis;
            }

            .gradient {
                position: absolute;
                height: 40px;
                left: 0;
                right: 0;
                bottom: 0;
                cursor: pointer;
                background: linear-gradient(to top, #ffffff, #ffffff00);

                .expandBtn {
                    position: absolute;
                    bottom: -5px;
                    right: 0;
                    font-size: 14px;
                    color: #00a1d6;
                }
            }
        }

        .reduce {
            font-size: 14px;
            color: #00a1d6;
            cursor: pointer;
        }
    }
}



.right-box {
    width: 100%;
    display: flex;
    flex-direction: column;
    border-radius: 10px;
    padding-inline: 10px;
    padding-bottom: 10px;

    margin-bottom: 15px;

    background-color: #f1f2f3;

    .right-box-title {
        display: flex;
        width: 100%;
        height: min(44px, 5vh);
        margin-top: calc((5vw - 20px)*.1);
        margin-bottom: calc(min(44px, 5vh)*.2);
        flex-direction: row;

        position: relative;

        .left {
            display: flex;
            align-items: center;
            width: 30%;
            height: min(44px, 5vh);
            position: absolute;
            left: calc((5vw - 20px)*.1);

            span {
                margin-left: 5px;
                font-size: 12px;
                color: #61666d;
            }
        }

        .right {
            display: flex;
            align-items: center;
            width: 30%;
            height: min(44px, 5vh);
            position: absolute;
            right: 0;
        }
    }

    .number-list {
        display: flex;
        flex-wrap: wrap;
        width: 100%;

        .number-list-item {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 4vw;
            height: 4vw;
            margin: calc((5vw - 20px)*.1);
            background-color: white;
            border-radius: 5px;
            box-sizing: border-box;
            user-select: none;
            cursor: pointer;
        }

        .number-list-item:hover {
            background-color: #dff6fd;
            color: #00a1d6;
            border: 1px solid #00a1d6;
        }

        .number-list-item.current {
            background-color: #00a1d6;
            color: white;
        }
    }
}
</style>
