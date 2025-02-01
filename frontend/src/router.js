import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/HomePage.vue';
import EventosPage from './views/EventosPage.vue';
import ReportesPage from './views/ReportesPage.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/eventos', component: EventosPage },
  { path: '/reportes', component: ReportesPage }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

