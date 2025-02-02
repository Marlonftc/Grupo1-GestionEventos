// 🔹 Importamos createRouter y createWebHistory desde Vue Router
import { createRouter, createWebHistory } from 'vue-router';

// 🔹 Importamos las vistas que serán utilizadas en las rutas
import HomePage from './views/HomePage.vue';
import EventosPage from './views/EventosPage.vue';
import ReportesPage from './views/ReportesPage.vue';

// 🔹 Definimos las rutas de la aplicación
const routes = [
  { path: '/', component: HomePage }, // Página principal
  { path: '/eventos', component: EventosPage }, // Página de eventos
  { path: '/reportes', component: ReportesPage } // Página de reportes
];

// 🔹 Creamos el enrutador con el historial de navegación basado en la API de HTML5
const router = createRouter({
  history: createWebHistory(), // 🔹 Usa createWebHistory para URLs limpias sin #
  routes
});

// 🔹 Exportamos el enrutador para que sea utilizado en la aplicación Vue
export default router;
