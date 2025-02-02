// 🔹 Importamos Vue y creamos la aplicación
import { createApp } from 'vue';
import App from './App.vue';

// 🔹 Importamos el enrutador para manejar la navegación entre páginas
import router from './router';

// 🔹 Importamos Bootstrap para los estilos y la funcionalidad de los componentes
import 'bootstrap/dist/css/bootstrap.min.css'; // Estilos de Bootstrap
import 'bootstrap/dist/js/bootstrap.bundle.min.js'; // Funcionalidades de Bootstrap como modales y tooltips

// 🔹 Creamos la instancia de la aplicación Vue
const app = createApp(App);

// 🔹 Registramos el enrutador en la aplicación
app.use(router);

// 🔹 Montamos la aplicación en el elemento con el ID 'app'
app.mount('#app');
