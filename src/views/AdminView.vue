<template>
    <div>
        <audio class="myPlayer" controls :src="audioSource" ref="audio"></audio>
        <div class="container">
            <ul class="lrcList" ref="lrcList">
                <li v-for="(item, index) in lrcData" :key="index" :class="{ current: index === currentIndex }">
                    {{ item.word }}
                </li>
            </ul>
        </div>
    </div>
</template>

<style>
ul,
li,
ol {
    list-style: none;
}

.myPlayer {
    display: block;
    width: 600px;
    margin-top: 50px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0.5;
    transition: all 0.2s;
}

.myPlayer:hover {
    opacity: 1;
}

.container {
    display: flex;
    width: 1200px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 30px;
    height: 300px;
    overflow: hidden;
    position: relative;
}

.lrcList {
    position: absolute;
    top: 0;
    font-size: 16px;
    line-height: 30px;
    color: #869cd3;
    text-align: center;
    transition: all 0.2s;
    width: 100%;
    height: 100%;
}

.lrcList li {
    transition: all 0.2s;
    height: 30px;
    opacity: 0.5;
}

.lrcList .current {
    transform: scale(1.4);
    color: #000000;
    opacity: 1;
}
</style>

<script>
export default {
    data() {
        return {
            audioSource: "http://ws.stream.qqmusic.qq.com/O8000032wpIs0D30HZ.ogg?guid=0&vkey=47EF1FB7FDC25085AA8772E2DBABAB2E1A0BD85F2B3910F2A41AF32E53052B391206F43C12BF0CCBE5B6ABB92E65DDF4D6D4A294D002F0EE&uin=2965422689&fromtag=119780&src=O8000042eWYv0a3Qi2.ogg",
            lrcData: [],
            currentIndex: 0,
        };
    },
    mounted() {
        this.parseLRC();
        this.setLrcListPosition();
        this.$refs.audio.addEventListener("timeupdate", this.handleTimeUpdate);
    },
    methods: {
        parseLRC() {
            const lrc = `[00:00.00]不眠之夜 (《崩坏：星穹铁道》匹诺康尼中文主题曲) - 张杰/HOYO-MiX\n[00:05.01]作词 Lyricist：李崎/往人不识\n[00:06.72]作曲 Composer：王可鑫 Eli.W (HOYO-MiX)\n[00:08.11]编曲 Arranger：崔瀚普TSAR (HOYO-MiX)\n[00:09.58]制作人 Producer：崔瀚普TSAR (HOYO-MiX)\n[00:15.74]车窗外 这夜色 流光溢彩\n[00:19.58]别忘了 闭上眼 才算醒来\n[00:23.57]你参演 这场戏 变换姿态\n[00:27.50]谜底 结局 我该 怎么猜\n[00:32.49]记忆是梦的开场白\n[00:36.08]（伤疤被掩盖 昨日还在）\n[00:40.44]时间在静候你醒来\n[00:46.76]（Take me away）\n[00:48.01]别再破碎 别再枯萎\n[00:51.76]继续沉醉 自我迂回\n[00:55.64]最后品味 永恒的滋味\n[00:58.98]下一场那夜的梦 再相会\n[01:03.92]越是虚伪 越是完美\n[01:07.77]美梦入睡 绝望轮回\n[01:11.74]一闭一睁 便开始倒退\n[01:14.94]下一场那夜的梦 再相会\n[01:24.13]（伏笔没解开 悬念还在）\n[01:28.37]时间在静候你醒来\n[01:34.86]（Sing with me）\n[01:36.00]别再破碎 别再枯萎\n[01:39.74]继续沉醉 自我迂回\n[01:43.74]最后品味 永恒的滋味\n[01:46.97]来一场不眠之夜 作结尾\n[01:52.05]越要快乐 越要破溃\n[01:55.76]是是非非 别再意会\n[01:59.75]忘记时间 来梦的派对\n[02:02.99]来一场不眠之夜 作结尾\n[02:08.16]人声 Vocal Artist：张杰\n[02:09.02]小号/富鲁格号 Trumpet/Flugelhorn：夏非\n[02:09.34]长号 Trombone：曹侃\n[02:09.51]录音棚 Recording Studio：未来•福录音室FUTURE•LIVE STUDIO/升赫录音棚Soundhub Studio\n[02:10.26]录音师 Recording Engineer：吴身宝 Bob Wu@Soundhub Studios/Kevin刘瀚文@Soundhub Studios\n[02:10.79]混音师 Mixing Engineer：崔瀚普TSAR (HOYO-MiX)\n[02:11.12]母带制作 Mastering Engineer：崔瀚普TSAR (HOYO-MiX)\n[02:12.20]出品 Produced by：HOYO-MiX`

            function parseTime(timer) {
                let t = timer.split(":");
                let result = Number(t[0]) * 60 + Number(t[1]);
                return result;
            }

            let lines = lrc.split('\n');
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
            console.log(this.lrcData)
        },
        setLrcListPosition() {
            const lrcList = this.$refs.lrcList;
            const liElements = lrcList.getElementsByTagName('li'); // 获取所有li元素

            const liHeight = liElements.length > 0 ? liElements[0].getBoundingClientRect().height : 0;
            const containerHeight = lrcList.parentElement.getBoundingClientRect().height;

            let dis = -1 * (this.currentIndex * liHeight + liHeight / 2 - containerHeight / 2);
            lrcList.style.transform = `translateY(${dis}px)`;
        },

        handleTimeUpdate() {
            let currentTime = this.$refs.audio.currentTime;
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
};
</script>
