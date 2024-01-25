<template>
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
                    <span class="author">歌手</span>
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
                <v-slider class="slider-bar" v-model="volume" color="white" hide-details="true" :thumb-size="15"></v-slider>
            </div>
            <button @click="max" class="maxBtn"><font-awesome-icon :icon="['fas', 'chevron-up']" /></button>
        </div>

        <div class="music-play">
        </div>
    </div>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlay, faPause, faStepForward, faStepBackward, faAngleLeft, faVolumeXmark, faVolumeHigh, faShuffle, faUpRightAndDownLeftFromCenter, faChevronUp } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faPlay, faPause, faStepForward, faStepBackward, faAngleLeft, faVolumeXmark, faVolumeHigh, faShuffle, faUpRightAndDownLeftFromCenter, faChevronUp)

export default {
    data() {
        return {
            isPlaying: false,
            isClick: false,
            volume: 50,
            prevVolume: 50,
            title: '歌名歌名歌名歌名歌名歌名歌名歌名歌名歌名歌名歌名歌名'
        };
    },
    components: {
        FontAwesomeIcon,
    },
    mounted() {
        //写music-play用，记得删
        this.max();
    },
    methods: {
        prev() {
        },
        toggle() {
            this.isPlaying = !this.isPlaying
        },
        next() {
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
        max() {
            const musicBar = document.querySelector('.music-bar');
            const musicPlay = document.querySelector('.music-play');
            const returnButton = document.querySelector('.returnBtn');

            if (!musicBar || !musicPlay || !returnButton) return;

            function handleKeydown(event) {
                if (event.keyCode === 27) {
                    if (musicBar.style.transform === '' && musicPlay.style.transform === '' && returnButton.style.transform === '') {
                        document.removeEventListener('keydown', handleKeydown);
                    } else {
                        musicBar.style.transition = 'transform 0.3s';
                        musicPlay.style.transition = 'transform 0.3s';
                        returnButton.style.transition = 'transform 0.3s';
                        setTimeout(() => {
                            musicBar.style.transform = '';
                            musicPlay.style.transform = '';
                            returnButton.style.transform = '';
                        }, 0);

                    }
                }
            }

            if (musicBar.style.transform === 'translateX(100vw)' && musicPlay.style.transform === 'translateX(-100vw)') {
                musicBar.style.transition = '';
                musicPlay.style.transition = '';
                setTimeout(() => {
                    musicBar.style.transform = '';
                    musicPlay.style.transform = '';
                    returnButton.style.transform = '';
                }, 300);
                document.addEventListener('keydown', handleKeydown);
            } else {
                musicBar.style.transition = 'transform 0.3s';
                musicPlay.style.transition = 'transform 0.3s';
                returnButton.style.transition = 'transform 0.3s';
                setTimeout(() => {
                    musicBar.style.transform = 'translateX(100vw)';
                    musicPlay.style.transform = 'translateX(-100vw)';
                    returnButton.style.transform = 'translateX(-10vw)';
                }, 0);
                document.addEventListener('keydown', handleKeydown);
            }
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
    backdrop-filter: blur(1000px);
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

.music-play {
    position: absolute;
    top: 0;
    left: 100vw;

    width: 100vw;
    height: 100vh;
    background-color: rgba(255, 255, 255, 0.4);
    z-index: 5;
}
</style>
