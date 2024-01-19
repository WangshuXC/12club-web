import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
      meta: {
        showNavBar: true
      },
    },
    {
      path: '/anime',
      name: 'anime',
      component: () => import('../views/AnimeView.vue'),
      meta: {
        showNavBar: true
      },
    },
    {
      path: '/animeplay',
      name: 'animeplay',
      component: () => import('../views/AnimePlay.vue'),
      meta: {
        showNavBar: true
      },
    },
    {
      path: '/comic',
      name: 'comic',
      component: () => import('../views/ComicView.vue'),
      meta: {
        showNavBar: true
      },
    },
    {
      path: '/novel',
      name: 'novel',
      component: () => import('../views/NovelView.vue'),
      meta: {
        showNavBar: true
      },
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
      meta: {
        showNavBar: true
      },
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminView.vue'),
      meta: {
        showNavBar: false
      },
    },
  ]
})

export default router
