import { createRouter, createWebHistory } from 'vue-router';
import ProfilePage from '../components/ProfilePage.vue';
import SchedulePage from '../components/SchedulePage.vue';
import AuthPage from '../components/AuthPage.vue'; // Импортируем компонент страницы регистрации

const routes = [
  { path: '/', redirect: '/auth' },
  { path: '/profile', component: ProfilePage },
  { path: '/schedule', component: SchedulePage },
  { path: '/auth', component: AuthPage } // Добавляем маршрут для страницы регистрации
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;