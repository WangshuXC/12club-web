<template>
    <audio ref="audioPlayer" :src="audioSrc" @timeupdate="updateProgress"></audio>
    <v-snackbar v-model="showSnackbar" :timeout="1000" rounded="pill" color="#fff" variant="tonal">
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
            <div class="music-bar-info">
                <img src="https://cdnimg.gamekee.com/wiki2.0/images/w_1920/h_1080/829/287349/2023/4/9/338318.jpg"
                    alt="专辑图片">
                <div class="music-info">
                    <span class="title">{{ title }}</span>
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
                    :thumb-size="15"></v-slider>
            </div>
            <button @click="max" class="maxBtn"><font-awesome-icon :icon="['fas', 'chevron-up']" /></button>
        </div>
        <div class="music-play-bg"></div>
        <div class="music-play">
            <div class="music-info">
                <img src="https://cdnimg.gamekee.com/wiki2.0/images/w_1920/h_1080/829/287349/2023/4/9/338318.jpg"
                    alt="专辑图片">
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
                    <v-slider v-model="progress" color="white" hide-details="true" :thumb-size="0"
                        @update:model-value="seekTo"></v-slider>
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
            isPlaying: true,
            isClick: false,
            showSnackbar: false,
            volume: 100,
            prevVolume: 100,
            progress: 0,
            audioSrc: "https://dl.stream.qqmusic.qq.com/C400000GMGpe4IYOjH.m4a?guid=9318367020&vkey=A584029AA25229AD05B198F3D8FB8D80DC61FF71A0045ADF8C031B916562ADAEC13C3C6ACAB1BD663FC35D09F8C66F1184D1F769EB7B944A&uin=1294673511&fromtag=120032",
            audioElement: null,
            title: '歌名歌名歌名歌名歌名歌名歌名歌名歌名歌名歌名歌名歌名',
            author: '歌手',
            currentTime1: '00:00',
            totalTime: '00:00'
        };
    },
    components: {
        FontAwesomeIcon,
    },
    mounted() {
        //写music-play用，记得删
        this.max();
        this.audioElement = this.$refs.audioPlayer;
        this.audioElement.autoplay = this.isPlaying;
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

            if (musicBar.style.transform === 'translateX(100vw)' && musicPlay.style.transform === 'translateX(-100vw)') {
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
                    musicPlay.style.transform = 'translateX(-100vw)';
                    musicPlayBg.style.transform = 'translateX(-100vw)';
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
        formatTime(time) {
            const minutes = Math.floor(time / 60);
            const seconds = Math.floor(time % 60);
            return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
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
}

.return {
    width: 100%;
    height: 100%;
}

.return svg {
    width: 100%;
    height: 100%;
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
}

.music-bar .music-bar-info {
    display: flex;
    align-items: center;
    position: absolute;
    left: 5vw;
    width: 20vw;
    height: 100%;
}

.music-bar .music-bar-info img {
    width: 5vw;
    height: 5vw;
    border-radius: 10px;
    object-fit: cover;
    pointer-events: none;
}

.music-bar .music-bar-info .music-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;

    width: 100%;
    margin-left: 5%;
}

.music-bar .music-bar-info .music-info .title {
    max-width: 100%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-bottom: 10px;
    font-size: larger;
}

.music-bar .music-bar-switch {
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 20%;
    height: 100%;
}

.music-bar .music-bar-switch button {
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

.music-bar .music-bar-switch svg {
    height: 100%;
}

.music-bar .music-bar-control {
    position: absolute;
    display: flex;
    align-items: center;
    right: 10vw;
    width: 15%;
    height: 100%;
}

.music-bar .music-bar-control .slider {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    width: 50%;
    height: 100%;
    margin-right: 5%;
}

.music-bar .music-bar-control .slider button {
    width: 10%;
    height: 30%;
    margin-inline: 13%;
}

.slider svg {
    height: 100%;
}

.music-bar .maxBtn {
    position: absolute;
    right: 5%;

    width: 3vh;
    height: 3vh;
    color: black;

    border: none;
    outline: none;
    cursor: pointer;

    z-index: 999;
}

.music-bar .maxBtn svg {
    height: 100%;
}

.music-play-bg {
    position: absolute;
    top: 0;
    left: 100vw;
    z-index: 2;
    width: 100vw;
    height: 100vh;

    background-image: url('https://cdnimg.gamekee.com/wiki2.0/images/w_1920/h_1080/829/287349/2023/4/9/338318.jpg');
    background-size: cover;
    filter: blur(30px);
}

.music-play {
    display: flex;
    align-items: center;
    position: absolute;
    top: 0;
    left: 100vw;
    z-index: 3;
    width: 100vw;
    height: 100vh;

    background-color: rgba(0, 0, 0, 0.3);
}

.music-play .music-info {
    position: absolute;
    top: 10vh;
    left: 15vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 80vh;
    width: 30vw;
}

.music-play .music-info img {
    width: 30vw;
    height: 30vw;
    border-radius: 10px;
    object-fit: cover;
    pointer-events: none;
    margin-bottom: 5%;
}

.music-play .music-info .info-bar {
    height: 10%;
    width: 100%;

    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.music-info .info-bar .info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    width: 60%;

    color: white;
}

.music-info .info-bar .title {
    width: 100%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: larger;
}

.volume-bar {
    display: flex;
    align-items: center;
    width: 30%;
    height: 100%;
}

.volume-bar button {
    height: 35%;
    margin-right: 5%;
}

.volume-bar button svg {
    height: 100%;
}

.music-info .progress-bar {
    display: flex;
    align-items: center;
    color: white;
    height: 5%;
    width: 100%;
    margin-block: 5%;
}

.music-info .switch {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    height: 10%;
    width: 70%;
}

.music-info .switch button {
    height: 30%;
    width: 40%;
}

.music-info .switch .play {
    height: 55%;
}

.music-info .switch .sw {
    height: 40%;
}

.music-info .switch button svg {
    height: 100%;
}
</style>
