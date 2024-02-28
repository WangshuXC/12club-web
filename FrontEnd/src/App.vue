<template>
  <div v-if="showNavBar" :class="['App-Header', { 'scroll-down': scrollDown }]">
    <NavBar></NavBar>
  </div>

  <div class="App-Container">
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
  },
  data() {
    return {
      scrollDown: false,
      lastScrollTop: 0,
    };
  },
  computed: {
    showNavBar() {
      const meta = this.$route.meta;
      return !meta || meta.showNavBar !== false;
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      const scrollTop = window.scrollY;
      this.scrollDown = scrollTop > this.lastScrollTop;
      this.lastScrollTop = scrollTop;
    },
  },
}
</script>


<style>
.App-Header {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  /* box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); */
  transition: margin-top 0.3s ease;
  z-index: 999;
}

.App-Header.scroll-down {
  margin-top: -9vh;
}

.App-Container {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;

  overflow: hidden;
}
</style>
