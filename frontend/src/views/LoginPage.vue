<template>
  <div class="container mt-5">
    <h1 class="mb-4 text-center">Iniciar Sesión</h1>

    <div class="card p-4">
      <form @submit.prevent="login">
        <div class="mb-3">
          <label for="username" class="form-label">Usuario</label>
          <input
            type="text"
            id="username"
            class="form-control"
            v-model="username"
            required
          />
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">Contraseña</label>
          <input
            type="password"
            id="password"
            class="form-control"
            v-model="password"
            required
          />
        </div>

        <button type="submit" class="btn btn-primary">Ingresar</button>
      </form>
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
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("/api/login", {
          username: this.username,
          password: this.password,
        });

        // ✅ Validación antes de acceder a response.data.token
        if (response && response.data && response.data.token) {
          localStorage.setItem("token", response.data.token);
          alert("✅ Inicio de sesión exitoso");
          this.$router.push("/eventos"); // Redirigir a la página de eventos
        } else {
          alert("⚠️ Error en el inicio de sesión: Respuesta inesperada");
        }
      } catch (error) {
        console.error("Error en login:", error);
        alert(`⚠️ Error al iniciar sesión: ${error.response?.data?.error || error.message}`);
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 400px;
}
</style>
