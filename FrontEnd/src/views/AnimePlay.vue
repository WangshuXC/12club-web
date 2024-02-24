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
                        :class="{ current: index + 1 == currentEpisode }">
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
                <img :src="coverUrl" alt="" class="cover">
                <div class="info">
                    <p class="title">{{ title }}</p>
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

            <div class="comment">
                <div class="comment-navbar">
                    <div class="title">
                        <p class="title-text">评论</p>
                        <p class="total-reply">666</p>
                    </div>
                    <div class="nav-sort">
                        <div class="hot-sort">最热</div>
                        <div class="part-symbol"></div>
                        <div class="time-sort">最新</div>
                    </div>
                </div>

                <div class="reply-box">
                    <div class="reply-box-warp" :style="{ backgroundColor: replyBoxBgColor }">
                        <textarea class="textarea" ref="textarea" placeholder="天青色等烟雨，评论区在等你" @click="onClickTextarea"
                            @mouseover="onMouseoverTextarea" @mouseout="onMouseoutTextarea" />
                    </div>

                    <div class="box-expand" :style="{ height: isClickedTextarea ? '32px' : '0' }">
                        <div class="send-btn">
                            <div class="send-text">发布</div>
                        </div>
                    </div>
                </div>

                <div class="white"></div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Plyr from 'plyr';
import 'plyr/dist/plyr.css';

export default {
    data() {
        return {
            videoUrl: '',
            coverUrl: '',
            replyBoxBgColor: '#f1f2f3',
            isClickedTextarea: false,
            episode: 10,
            currentEpisode: 1,
            episodeNameList: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            downloadedIndex: [],
            dragging: false,
            isOver: false,
            isExpand: false,
            isNeedExpand: false,
            title: "鬼灭之刃",
            update_date: "2024-02-06 15:22:38",
            view_count: 6666,
            download_count: 666,
            description: ``,
        };
    },
    onLoad() {
        this.initBangumiData();
        this.initPlayer();
    },
    mounted() {
        this.$nextTick(() => {
            var introduction = this.$refs.introductionRef;
            if (introduction.scrollHeight > introduction.clientHeight) {
                this.isNeedExpand = true;
            } else {
                this.isNeedExpand = false;
            }
        });
        document.addEventListener('click', () => {
            this.isClickedTextarea = false;
            this.replyBoxBgColor = '#f1f2f3';
        });
    },
    methods: {
        initBangumiData() {
            var currentUrl = window.location.href;
            var urlParts = currentUrl.split('/');
            var animeid = urlParts[urlParts.length - 1];

            let requestUrl = `http://127.0.0.1:5000/api/anime/${animeid}`;
            axios.get(requestUrl)
                .then(response => {
                    this.title = response.data.title;
                    this.videoUrl = `http://127.0.0.1:3000/anime/${response.data.title}/1.mp4`
                    this.coverUrl = `http://127.0.0.1:3000/anime/${response.data.title}/Cover.jpg`
                    this.episode = response.data.episode_count;
                    this.description = response.data.description;
                    this.isOver = response.data.isover;
                    this.update_date = response.data.update_date.replace('T', ' ');
                    this.view_count = response.data.view_count;
                    this.download_count = response.data.download_count;
                })
                .catch(error => {
                    console.error("There was an error fetching the anime data:", error);
                });
        },
        initPlayer() {
            this.player = new Plyr('#player', {
                controls: ['play-large', 'play', 'progress', 'current-time', 'mute', 'volume', 'settings', 'download', 'pip', 'fullscreen'],
                speed: { selected: 1, options: [0.5, 0.75, 1, 1.25, 1.5, 2] },
                autoplay: false,
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
        },
        adjustTextareaHeight() {
            const textarea = this.$refs.textarea;
            textarea.style.height = 'auto';

            const lineHeight = parseFloat(getComputedStyle(textarea).lineHeight);
            const lines = textarea.scrollHeight / lineHeight;
            const newHeight = lines * lineHeight;

            textarea.style.height = `${newHeight}px`;
        },
        onClickTextarea(event) {
            this.replyBoxBgColor = 'transparent';
            this.isClickedTextarea = true;
            event.stopPropagation();
        },
        onMouseoverTextarea() {
            if (!this.isClickedTextarea) {
                this.replyBoxBgColor = 'transparent';
            }
        },
        onMouseoutTextarea() {
            if (!this.isClickedTextarea) {
                this.replyBoxBgColor = '#f1f2f3';
            }
        },
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

    .comment {
        width: 100%;
        min-height: 20vh;
        margin-top: 5vh;
        display: flex;
        flex-direction: column;

        .comment-navbar {
            display: flex;
            align-items: center;
            width: 100%;

            .title {
                display: flex;
                align-items: center;
                font-size: 20px;
                color: #9499a0;

                .title-text {
                    color: #18191c;
                    font-weight: 500;
                }

                .total-reply {
                    font-size: 13px;
                    margin: 0 36px 0 6px;
                }
            }

            .nav-sort {
                display: flex;
                align-items: center;
                font-size: 13px;
                color: #9499a0;

                .hot-sort {
                    cursor: pointer;
                }

                .part-symbol {
                    height: 11px;
                    margin: 0 12px;
                    border-left: solid 1px;
                }

                .time-sort {
                    cursor: pointer;
                }
            }
        }

        .reply-box {
            display: flex;
            flex-direction: column;
            width: 100%;
            margin-top: 3vh;

            .reply-box-warp {
                display: flex;
                position: relative;
                min-height: 48px;
                transition: .2s;
                border: 1px solid #E3E5E7;
                border-radius: 6px;
                overflow: hidden;

                z-index: 2;

                .textarea {
                    width: 100%;
                    min-height: 32px;
                    max-height: 96px;
                    cursor: text;
                    border: none;
                    border-radius: 6px;
                    background-color: transparent;
                    margin: 6px 0px 6px 6px;
                    padding-right: 6px;
                    font-size: 14px;
                    resize: none;
                    outline: none;
                }

                .textarea::-webkit-scrollbar {
                    width: 8px;
                    background-color: transparent;
                }

                .textarea::-webkit-scrollbar-thumb {
                    background-color: rgba(0, 0, 0, 0.2);
                    border-radius: 4px;
                }
            }

            .box-expand {
                width: 100%;
                height: 0px;
                margin-top: 2vh;
                transition: all .2s ease-in-out;

                .send-btn {
                    float: right;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    position: relative;
                    width: 70px;
                    height: 100%;
                    border-radius: 6px;
                    cursor: pointer;
                    background-color: #7fd6f5;

                    .send-text {
                        position: absolute;
                        font-size: 16px;
                        color: white;
                    }
                }

                .send-btn:hover {
                    background-color: #00a1d6;
                }
            }
        }

        .white {
            width: 100%;
            height: 30vh;
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
