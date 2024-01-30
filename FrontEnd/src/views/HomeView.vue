<template>
    <div class="ibanner" ref="ibanner">
        <div class="sub-div-container">
            <div v-for="(item, index) in items" :key="index" class="sub-div"
                :style="{ backgroundImage: `url(${item.background})` }">
                {{ item.text }}
            </div>
        </div>
    </div>
    <div class="lalala"></div>
</template>

<script>
export default {
    data() {
        return {
            items: [
                { text: 'Item 1', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/196838.jpg' },
                { text: 'Item 2', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/268101.jpg' },
                { text: 'Item 3', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/179540.jpg' },
                { text: 'Item 4', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/138165.jpg' },
                { text: 'Item 5', background: 'https://cdnimg.gamekee.com/wiki2.0/images/w_1600/h_1124/829/287349/2023/4/9/793597.jpg' }
            ]
        }
    },
    mounted() {
        const ibanner = this.$refs.ibanner;
        const subDivContainer = ibanner.querySelector('.sub-div-container');
        const ibannerWidth = ibanner.offsetWidth;

        subDivContainer.style.width = `${ibannerWidth * this.items.length}px`;

        const animate = () => {
            setTimeout(() => {
                subDivContainer.style.transform = `translateX(-${ibannerWidth}px)`;
                setTimeout(() => {
                    subDivContainer.style.transition = 'transform 0s';
                    this.items.push(this.items.shift());
                    subDivContainer.style.transform = '';
                    animate();
                }, 1000);
                subDivContainer.style.transition = 'transform 0.5s ease-out';
            }, 2000);
        };

        animate();
    }
}
</script>

<style>
* {
    overflow-x: hidden;
}

.ibanner {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
}

.sub-div-container {
    display: flex;
    width: 100%;
    height: 100%;
    transition: transform 0.5s ease;
}

.sub-div {
    flex: 1;
    width: 100vw;
    height: 100vh;
    color: #ffffff;
    text-align: center;
    font-size: 54px;
    line-height: 100vh;
    background-size: cover;
    background-position: center center;
}

.lalala {
    height: 100vh;
    width: 100vw;
}
</style>
