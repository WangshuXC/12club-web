<template>
    <div class="video-player">
        <video id="player" playsinline controls>
            <source :src="videoUrl">
        </video>
    </div>
</template>

<script>
import Plyr from 'plyr';
import 'plyr/dist/plyr.css';

export default {
    data() {
        return {
            videoUrl: 'http://127.0.0.1:3000/anime/药屋少女的呢喃/2.mp4'
            // videoUrl: 'http://127.0.0.1:3000/anime/我心里危险的东西/2.mkv'
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
    },
};
</script>

<style>
.video-player {
    margin-top: 10vh;
    margin-left: 5%;
    width: 80vw;
    height: 75vh;
    display: flex;
}
</style>
