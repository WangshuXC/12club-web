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
        };
    },
    mounted() {
        this.initPlayer();
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

        background-color: #61666d;

        position: absolute;
        left: 0;
        top: calc(68vw*.5625 + 5vh);
    }
}

.left-box-container {
    .media-info {
        width: 100%;
        height: calc(68vw*.25);
        display: flex;
        justify-content: space-between;
        background-color: antiquewhite;
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
