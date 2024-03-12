import { createRouter, createWebHistory } from 'vue-router'

// function checkTokenAndRedirect(to, from, next) {
//   const isLoggedIn = localStorage.getItem('token');

//   if (isLoggedIn) {
//     // 如果 token 存在，可以发送请求到后端验证 token 的有效性
//     // 省略实际的 token 验证过程
//     // 假设验证通过，则继续导航到目标页面
//     next();
//   } else {
//     // 如果 token 不存在，跳转到登录页
//     next('/admin');
//   }
// }

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
      // beforeEnter: checkTokenAndRedirect()
    },
    {
      path: '/admin/op',
      name: 'adminOp',
      component: () => import('../views/AdminView.vue'),
      meta: {
        showNavBar: true
      },
      // beforeEnter: checkTokenAndRedirect()
    }
  ]
})

export default router
