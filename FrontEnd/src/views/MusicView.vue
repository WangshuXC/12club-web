<template>
    <audio ref="audioPlayer" :src="audioSrc" @timeupdate="updateProgress"></audio>
    <v-snackbar v-model="showSnackbar" :timeout="2000" rounded="pill" color="#fff" variant="tonal">
        按下esc退出全屏
    </v-snackbar>
    <div class="music-view">
        <a href="/" class="returnBtn">
            <button class="return"><font-awesome-icon :icon="['fas', 'angle-left']" /></button>
        </a>
        <div class="music-background"></div>
        <div class="music-background-mask"></div>
        <div class="music-index"></div>
        <div class="music-bar">
            <v-slider class="progress-bar" v-model="progress" color="grey" hide-details="true" :thumb-size="thumbSize"
                @update:model-value="seekTo" @mouseover="handleMouseOver" @mouseout="handleMouseOut"></v-slider>
            <div class="music-bar-info">
                <img :src='albumCover' alt="专辑图片">
                <div class="music-info">
                    <span class="title"><strong>{{ title }}</strong></span>
                    <span class="author">{{ author }}</span>
                </div>
            </div>
            <div class="music-bar-switch">
                <button @click="prev"><font-awesome-icon :icon="['fas', 'step-backward']" /></button>
                <button @click="toggle"><font-awesome-icon
                        :icon="isPlaying ? ['fas', 'pause'] : ['fas', 'play']" /></button>
                <button @click="next"><font-awesome-icon :icon="['fas', 'step-forward']" /></button>
            </div>
            <div class="music-bar-control">
                <div class="slider">
                    <button @click="mode_toggle" class="modeBtn"><font-awesome-icon :icon="['fas', 'shuffle']" /></button>
                    <button @click="volume_toggle"><font-awesome-icon
                            :icon="isXmark ? ['fas', 'volume-xmark'] : ['fas', 'volume-high']" /></button>
                </div>
                <v-slider v-model="volume" color="white" hide-details="true" @update:model-value="setVolume"
                    :thumb-size="10"></v-slider>
            </div>
            <button @click="max" class="maxBtn"><font-awesome-icon :icon="['fas', 'chevron-up']" /></button>
        </div>

        <div class="music-play-bg" :style="{ backgroundImage: 'url(' + albumCover + ')' }"></div>
        <div class="music-play">
            <div class="music-info">
                <img :src='albumCover' alt="专辑图片">
                <div class="info-bar">
                    <div class="info">
                        <span class="title"><strong>{{ title }}</strong></span>
                        <span class="author">{{ author }}</span>
                    </div>
                    <div class="volume-bar">
                        <button @click="volume_toggle"><font-awesome-icon
                                :icon="isXmark ? ['fas', 'volume-xmark'] : ['fas', 'volume-high']" /></button>
                        <v-slider v-model="volume" color="white" hide-details="true" @update:model-value="setVolume"
                            :thumb-size="10"></v-slider>
                    </div>
                </div>
                <div class="progress-bar">
                    <strong>{{ currentTime1 }}</strong>
                    <v-slider v-model="progress" color="white" hide-details="true" :thumb-size="thumbSize"
                        @update:model-value="seekTo" @mouseover="handleMouseOver" @mouseout="handleMouseOut"></v-slider>
                    <strong>{{ totalTime }}</strong>
                </div>
                <div class="switch">
                    <button @click="mode_toggle" class="modeBtn"><font-awesome-icon :icon="['fas', 'shuffle']" /></button>
                    <button @click="prev" class="sw"><font-awesome-icon :icon="['fas', 'step-backward']" /></button>
                    <button @click="toggle" class="play"><font-awesome-icon
                            :icon="isPlaying ? ['fas', 'pause'] : ['fas', 'play']" /></button>
                    <button @click="next" class="sw"><font-awesome-icon :icon="['fas', 'step-forward']" /></button>
                    <button @click="like"><font-awesome-icon :icon="['fas', 'heart']" /></button>
                </div>
            </div>

            <div class="music-lrc">
                <ul class="lrcList" ref="lrcList">
                    <li v-for="(item, index) in lrcData" :key="index" :class="{ current: index === currentIndex }">
                        {{ item.word }}
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlay, faPause, faStepForward, faStepBackward, faAngleLeft, faVolumeXmark, faVolumeHigh, faShuffle, faUpRightAndDownLeftFromCenter, faChevronUp, faHeart } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faPlay, faPause, faStepForward, faStepBackward, faAngleLeft, faVolumeXmark, faVolumeHigh, faShuffle, faUpRightAndDownLeftFromCenter, faChevronUp, faHeart)

export default {
    data() {
        return {
            isPlaying: false,
            isClick: false,
            showSnackbar: false,
            volume: 100,
            prevVolume: 100,
            progress: 0,
            thumbSize: 0,
            audioSrc: "http://127.0.0.1:3000/music/%E4%B8%8D%E7%9C%A0%E4%B9%8B%E5%A4%9C/%E5%BC%A0%E6%9D%B0&HOYO-MiX%20-%20%E4%B8%8D%E7%9C%A0%E4%B9%8B%E5%A4%9C.mp3",
            audioElement: null,
            title: '不眠之夜',
            author: '张杰/HOYO-MiX',
            currentTime1: '00:00',
            totalTime: '00:00',
            lrcData: [],
            currentIndex: 0,
            lrc: `[00:00.00]作词 Lyricist：李崎/往人不识\n[00:06.72]作曲 Composer：王可鑫 Eli.W (HOYO-MiX)\n[00:08.11]编曲 Arranger：崔瀚普TSAR (HOYO-MiX)\n[00:09.58]制作人 Producer：崔瀚普TSAR (HOYO-MiX)\n[00:15.74]车窗外 这夜色 流光溢彩\n[00:19.58]别忘了 闭上眼 才算醒来\n[00:23.57]你参演 这场戏 变换姿态\n[00:27.50]谜底 结局 我该 怎么猜\n[00:32.49]记忆是梦的开场白\n[00:36.08]（伤疤被掩盖 昨日还在）\n[00:40.44]时间在静候你醒来\n[00:46.76]（Take me away）\n[00:48.01]别再破碎 别再枯萎\n[00:51.76]继续沉醉 自我迂回\n[00:55.64]最后品味 永恒的滋味\n[00:58.98]下一场那夜的梦 再相会\n[01:03.92]越是虚伪 越是完美\n[01:07.77]美梦入睡 绝望轮回\n[01:11.74]一闭一睁 便开始倒退\n[01:14.94]下一场那夜的梦 再相会\n[01:24.13]（伏笔没解开 悬念还在）\n[01:28.37]时间在静候你醒来\n[01:34.86]（Sing with me）\n[01:36.00]别再破碎 别再枯萎\n[01:39.74]继续沉醉 自我迂回\n[01:43.74]最后品味 永恒的滋味\n[01:46.97]来一场不眠之夜 作结尾\n[01:52.05]越要快乐 越要破溃\n[01:55.76]是是非非 别再意会\n[01:59.75]忘记时间 来梦的派对\n[02:02.99]来一场不眠之夜 作结尾\n[02:08.16]人声 Vocal Artist：张杰\n[02:09.02]小号/富鲁格号 Trumpet/Flugelhorn：夏非\n[02:09.34]长号 Trombone：曹侃\n[02:09.51]录音棚 Recording Studio：未来•福录音室FUTURE•LIVE STUDIO/升赫录音棚Soundhub Studio\n[02:10.26]录音师 Recording Engineer：吴身宝 Bob Wu@Soundhub Studios/Kevin刘瀚文@Soundhub Studios\n[02:10.79]混音师 Mixing Engineer：崔瀚普TSAR (HOYO-MiX)\n[02:11.12]母带制作 Mastering Engineer：崔瀚普TSAR (HOYO-MiX)\n[02:12.20]出品 Produced by：HOYO-MiX`,
            albumCover: 'https://y.qq.com/music/photo_new/T002R800x800M000004ItRwk3R0LYz.jpg'
        };
    },
    components: {
        FontAwesomeIcon,
    },
    mounted() {
        this.parseLRC();
        this.audioElement = this.$refs.audioPlayer;
        this.audioElement.autoplay = this.isPlaying;
        this.audioElement.addEventListener("timeupdate", this.handleTimeUpdate);
        this.audioElement.addEventListener('loadedmetadata', () => {
            this.totalTime = this.formatTime(this.audioElement.duration);
        });

    },
    methods: {
        prev() {
        },
        toggle() {
            if (this.isPlaying) {
                this.audioElement.pause();
            } else {
                this.audioElement.play();
            }
            this.isPlaying = !this.isPlaying
        },
        next() {
        },
        like() {
        },
        volume_toggle() {
            if (this.volume !== 0) {
                this.prevVolume = this.volume
                this.isClick = false
                this.volume = 0
            }
            else {
                this.isClick = true
                this.volume = this.prevVolume
            }
            this.setVolume()
        },
        setVolume() {
            this.audioElement.volume = this.volume / 100;
        },
        max() {
            const musicBar = document.querySelector('.music-bar');
            const musicPlay = document.querySelector('.music-play');
            const musicPlayBg = document.querySelector('.music-play-bg');
            const returnButton = document.querySelector('.returnBtn');

            if (!musicBar || !musicPlay || !musicPlayBg || !returnButton) return;
            this.showSnackbar = true;
            function handleKeydown(event) {
                if (event.keyCode === 27) {
                    this.showSnackbar = false;
                    if (musicBar.style.transform === '' && musicPlay.style.transform === '') {
                        document.removeEventListener('keydown', handleKeydown);
                    } else {
                        musicBar.style.transition = 'transform 0.3s';
                        musicPlay.style.transition = 'transform 0.3s';
                        musicPlayBg.style.transition = 'transform 0.3s';
                        returnButton.style.transition = 'transform 0.3s';
                        setTimeout(() => {
                            musicBar.style.transform = '';
                            musicPlay.style.transform = '';
                            musicPlayBg.style.transform = '';
                            returnButton.style.transform = '';
                        }, 0);
                    }
                }
            }

            if (musicBar.style.transform === 'translateX(100vw)' && musicPlay.style.transform === 'translateX(-200vw)') {
                musicBar.style.transition = '';
                musicPlay.style.transition = '';
                musicPlayBg.style.transition = '';
                returnButton.style.transition = '';
                setTimeout(() => {
                    musicBar.style.transform = '';
                    musicPlay.style.transform = '';
                    musicPlayBg.style.transform = '';
                    returnButton.style.transform = '';
                }, 300);
                document.addEventListener('keydown', handleKeydown);
            } else {
                musicBar.style.transition = 'transform 0.3s';
                musicPlay.style.transition = 'transform 0.3s';
                musicPlayBg.style.transition = 'transform 0.3s';
                returnButton.style.transition = 'transform 0.3s';
                setTimeout(() => {
                    musicBar.style.transform = 'translateX(100vw)';
                    musicPlay.style.transform = 'translateX(-200vw)';
                    musicPlayBg.style.transform = 'translateX(-200vw)';
                    returnButton.style.transform = 'translateX(-10vw)';
                }, 0);
                document.addEventListener('keydown', handleKeydown);
            }
        },
        updateProgress() {
            const currentTime = this.audioElement.currentTime;
            const duration = this.audioElement.duration;
            this.progress = (currentTime / duration) * 100;
            this.currentTime1 = this.formatTime(this.audioElement.currentTime);
        },
        seekTo(value) {
            const duration = this.audioElement.duration;
            const seekTime = (value / 100) * duration;
            this.audioElement.currentTime = seekTime;
        },
        handleMouseOver() {
            this.thumbSize = 10;
        },
        handleMouseOut() {
            this.thumbSize = 0;
        },
        formatTime(time) {
            const minutes = Math.floor(time / 60);
            const seconds = Math.floor(time % 60);
            return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        },
        parseLRC() {
            function parseTime(timer) {
                let t = timer.split(":");
                let result = Number(t[0]) * 60 + Number(t[1]);
                return result;
            }

            let lines = this.lrc.split('\n');
            let lrcArr = [];
            lines.forEach(item => {
                let result = item.trim().replace(/^\[/, "");
                let parts = result.split("]");
                let timer = parts[0].slice(1).trim();
                let obj = {
                    time: parseTime(timer),
                    word: parts[1] ? parts[1].trim() : ""
                };
                lrcArr.push(obj);
            });
            this.lrcData = lrcArr;
        },
        setLrcListPosition() {
            const lrcList = this.$refs.lrcList;
            const liElements = lrcList.getElementsByTagName('li');

            const liHeight = liElements.length > 0 ? liElements[0].getBoundingClientRect().height + 20 : 0;
            const containerHeight = lrcList.parentElement.getBoundingClientRect().height;

            let dis = -1 * (this.currentIndex * liHeight + liHeight / 2 - containerHeight / 2);
            if (dis <= 0) {
                lrcList.style.transform = `translateY(${dis}px)`;
            }
        },
        handleTimeUpdate() {
            let currentTime = this.$refs.audioPlayer.currentTime;
            for (let i = 0; i < this.lrcData.length; i++) {
                if (currentTime < this.lrcData[i].time) {
                    this.currentIndex = i - 1;
                    this.setLrcListPosition();
                    return;
                }
            }
            this.currentIndex = this.lrcData.length - 1;
            this.setLrcListPosition();
        }
    },
    computed: {
        isXmark() {
            return this.volume === 0;
        },
    },
    watch: {
        volume(newValue) {
            if (newValue === 0 && this.isClick) {
                this.prevVolume = 0
            }
        }
    }
}
</script>

<style>
html {
    overflow-y: hidden;
}

ul,
li,
ol {
    list-style: none;
}

svg :hover {
    color: #d3d1d2;
}

svg {
    color: #ffffff;
}

.returnBtn {
    width: 3vw;
    height: 3vw;
    position: absolute;
    top: 2vw;
    left: 4vw;

    z-index: 999;

    background-color: transparent;
    border: none;
    outline: none;
    cursor: pointer;

    .return {
        width: 100%;
        height: 100%;
    }

    .return svg {
        width: 100%;
        height: 100%;
    }
}

.music-background {
    position: fixed;
    top: 0;
    width: 100vw;
    height: 100vh;
    z-index: 1;
    background-image: url('../assets/imgs/music-background.jpg');
    background-size: cover;
    filter: blur(10px);
}

.music-background-mask {
    position: fixed;
    top: 0;
    width: 100vw;
    height: 100vh;
    z-index: 2;
    background-color: rgba(255, 255, 255, 0.703);
}

.music-bar {
    display: flex;
    justify-content: center;
    align-items: center;

    height: 10vh;
    width: 100vw;

    background-color: rgba(180, 180, 180, 0.4);

    position: absolute;
    top: 90vh;

    border-top-left-radius: 10px;
    border-top-right-radius: 10px;

    z-index: 999;

    .progress-bar {
        position: absolute;
        top: -18px;
        left: 3%;
        width: 94%;
        height: 10px;
    }

    .music-bar-info {
        display: flex;
        align-items: center;
        position: absolute;
        left: 5vw;
        width: 20vw;
        height: 100%;

        img {
            width: 5vw;
            height: 5vw;
            border-radius: 10px;
            object-fit: cover;
            pointer-events: none;
            user-select: none;
        }

        .music-info {
            display: flex;
            flex-direction: column;
            align-items: flex-start;

            width: 100%;
            margin-left: 5%;
            color: white;
            /* text-shadow: 1px 1px 1px black; */


            .title {
                max-width: 100%;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                margin-bottom: 10px;
                font-size: larger;
            }

            .author {
                font-size: smaller;
            }
        }
    }

    .music-bar-switch {
        display: flex;
        justify-content: space-around;
        align-items: center;
        width: 20%;
        height: 100%;

        button {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50%;
            width: 10%;
            background-color: transparent;
            border: none;
            outline: none;
            cursor: pointer;
        }

        svg {
            height: 100%;
        }
    }

    .music-bar-control {
        position: absolute;
        display: flex;
        align-items: center;
        right: 10vw;
        width: 15%;
        height: 100%;

        .slider {
            display: flex;
            justify-content: flex-end;
            align-items: center;
            width: 50%;
            height: 100%;
            margin-right: 5%;

            button {
                width: 10%;
                height: 30%;
                margin-inline: 13%;
            }

            svg {
                height: 100%;
            }
        }
    }

    .maxBtn {
        position: absolute;
        right: 5%;

        width: 3vh;
        height: 3vh;
        color: black;

        border: none;
        outline: none;
        cursor: pointer;

        z-index: 999;

        svg {
            height: 100%;
        }
    }
}

.music-play-bg {
    position: absolute;
    top: 0;
    left: 200vw;
    z-index: 2;
    width: 100vw;
    height: 100vh;

    background-size: cover;
    filter: blur(30px);
}

.music-play {
    display: flex;
    align-items: center;
    position: absolute;
    top: 0;
    left: 200vw;
    z-index: 3;
    width: 100vw;
    height: 100vh;

    background-color: rgba(0, 0, 0, 0.3);

    .music-info {
        position: absolute;
        top: 10vh;
        left: 15vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 80vh;
        width: 30vw;

        img {
            width: 30vw;
            height: 30vw;
            border-radius: 10px;
            object-fit: cover;
            pointer-events: none;
            margin-bottom: 5%;
            user-select: none;
        }

        .info-bar {
            height: 10%;
            width: 100%;

            display: flex;
            flex-direction: row;
            justify-content: space-between;

            .info {
                display: flex;
                flex-direction: column;
                justify-content: center;
                height: 100%;
                width: 60%;

                color: white;
            }

            .title {
                width: 100%;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                font-size: larger;
            }

            .author {
                font-size: smaller;
            }

            .volume-bar {
                display: flex;
                align-items: center;
                width: 30%;
                height: 100%;

                button {
                    height: 35%;
                    margin-right: 5%;

                    svg {
                        height: 100%;
                    }
                }
            }
        }

        .progress-bar {
            display: flex;
            align-items: center;
            color: white;
            height: 5%;
            width: 100%;
            margin-block: 5%;
        }

        .switch {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;

            height: 10%;
            width: 70%;

            button {
                height: 30%;
                width: 40%;

                svg {
                    height: 100%;
                }
            }

            .play {
                height: 55%;
            }

            .sw {
                height: 40%;
            }
        }
    }

    .music-lrc {
        overflow: hidden;
        position: absolute;
        top: 10vh;
        right: 10vw;

        width: 40vw;
        height: 80vh;

        .lrcList {
            position: absolute;
            top: 0;
            font-size: 16px;
            line-height: 30px;
            color: #ffffffa8;
            text-align: center;
            transition: all 0.2s;
            width: 100%;
            height: 100%;
        }

        .lrcList li {
            transition: all 0.2s;
            height: 30px;
            width: 100%;
            opacity: 0.5;
            margin-bottom: 20px;
        }

        .lrcList .current {
            transform: scale(1.7);
            color: #ffffff;
            width: 100%;
            opacity: 1;
        }
    }
}
</style>
