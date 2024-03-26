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
      path: '/animeplay/:anime_id',
      name: 'animeplay',
      component: () => import('../views/AnimePlay.vue'),
      meta: {
        showNavBar: true
      },
      props: true
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
        showNavBar: false
      },
    },
    {
      path: '/music',
      name: 'music',
      component: () => import('../views/MusicView.vue'),
      meta: {
        showNavBar: false
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
      component: () => import('../views/AdminLoginView.vue'),
      meta: {
        showNavBar: false
      },
    },
    {
      path: '/admin/op',
      name: 'adminOp',
      component: () => import('../views/AdminView.vue'),
      meta: {
        showNavBar: false,
      },
      beforeEnter: (to, from, next) => {
        const access_token = getCookie('access_token_cookie');
        const refresh_token = getCookie('refresh_token_cookie');

        if (!access_token || !refresh_token) {
          // 如果没有 access_token 或 refresh_token，重定向到 /admin 页面
          next('/admin');
        } else {
          // 如果有 access_token 和 refresh_token，则允许进入 admin/op 页面
          next();
        }
      },
    }
  ]
})
export default router

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}