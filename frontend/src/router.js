// 🔹 Importamos createRouter y createWebHistory desde Vue Router
import { createRouter, createWebHistory } from "vue-router";

// 🔹 Importamos las vistas que serán utilizadas en las rutas
import HomePage from "@/views/HomePage.vue";
import EventosPage from "@/views/EventosPage.vue";
import ReportesPage from "@/views/ReportesPage.vue";

// 🔹 Definimos las rutas de la aplicación
const routes = [
  { path: "/", component: HomePage }, // Página principal
  { path: "/eventos", component: EventosPage, meta: { requiresAuth: true } }, // 🔹 Página protegida
  { path: "/reportes", component: ReportesPage, meta: { requiresAuth: true } } // 🔹 Página protegida
];

// 🔹 Creamos el enrutador con historial de navegación limpio
const router = createRouter({
  history: createWebHistory(),
  routes
});

// 🔹 Proteger las rutas con un middleware de autenticación
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token"); // Obtener el token del localStorage

  // 🔹 Si la ruta requiere autenticación y no hay token, redirigir al login
  if (to.meta.requiresAuth && !token) {
    next("/login");
  } else {
    next(); // 🔹 Si el usuario tiene token o la ruta no necesita auth, continuar
  }
});

// 🔹 Exportamos el enrutador para usarlo en la aplicación Vue
export default router;
