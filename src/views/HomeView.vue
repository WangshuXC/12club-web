<template>
    <div class="ibanner" ref="ibanner">
        <div class="sub-div-container">
            <div v-for="(item, index) in items" :key="index" class="sub-div" :style="{ backgroundColor: item.color }">
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
                { text: 'Item 1', color: '#ff0000' },
                { text: 'Item 2', color: '#00ff00' },
                { text: 'Item 3', color: '#0000ff' },
                { text: 'Item 4', color: '#ffff00' },
                { text: 'Item 5', color: '#00ffff' }
            ]
        }
    },
    mounted() {
        const ibanner = this.$refs.ibanner;
        const subDivContainer = ibanner.querySelector('.sub-div-container');
        const ibannerWidth = ibanner.offsetWidth; // 获取ibanner的宽度

        subDivContainer.style.width = `${ibannerWidth * this.items.length}px`; // 设置sub-div-container的宽度为所有子div的总宽度

        const animate = () => {
            setTimeout(() => {
                subDivContainer.style.transform = `translateX(-${ibannerWidth}px)`;
                setTimeout(() => {
                    subDivContainer.style.transition = 'transform 0s';
                    this.items.push(this.items.shift()); // 将第一个子div移到最后
                    subDivContainer.style.transform = '';
                    animate();
                }, 1000); // 0.5秒后更新数据和清除变换
                subDivContainer.style.transition = 'transform 0.5s ease-out';
            }, 2000); // 1秒后开始平移变换
        };

        animate(); // 开始动画
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
    color: #000000;
    text-align: center;
    font-size: 54px;
    line-height: 100vh;
}

.lalala {
    height: 100vh;
    width: 100vw;
}
</style>
