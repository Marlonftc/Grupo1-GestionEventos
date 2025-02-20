<template>
  <div class="container text-center mt-5">
    <h1>Bienvenido a Gestión de Eventos</h1>
    <p>Administra tus eventos de forma eficiente con nuestro sistema.</p>

    <!-- 🔹 Formulario de Inicio de Sesión -->
    <div v-if="!isAuthenticated" class="card p-4 mx-auto mt-4" style="max-width: 400px;">
      <h3 class="mb-3">Iniciar Sesión</h3>
      <form @submit.prevent="login">
        <div class="mb-3">
          <label class="form-label">Usuario</label>
          <input type="text" class="form-control" v-model="username" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Contraseña</label>
          <input type="password" class="form-control" v-model="password" required />
        </div>
        <button type="submit" class="btn btn-primary">Ingresar</button>
      </form>
    </div>

    <!-- 🔹 Mostrar mensaje si ya está autenticado -->
    <div v-else class="mt-4">
      <h4>✅ Ya has iniciado sesión</h4>
      <button class="btn btn-danger" @click="logout">Cerrar Sesión</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      isAuthenticated: !!localStorage.getItem("token"), // 🔹 Verifica si hay un token
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("http://localhost:5000/login", {
          username: this.username,
          password: this.password,
        });

        localStorage.setItem("token", response.data.token);
        this.isAuthenticated = true; // 🔹 Actualiza el estado
        alert("✅ Inicio de sesión exitoso");
        this.$router.push("/eventos"); // Redirigir a eventos
      } catch (error) {
        alert("⚠ Error al iniciar sesión: " + (error.response?.data?.msg || "Intenta nuevamente"));
      }
    },
    logout() {
      localStorage.removeItem("token");
      this.isAuthenticated = false;
      alert("❌ Sesión cerrada");
    },
  },
};
</script>
