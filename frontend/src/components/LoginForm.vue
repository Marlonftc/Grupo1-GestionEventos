<template>
  <div class="container mt-5">
    <h2 class="text-center">Iniciar Sesión</h2>
    <div class="card p-4">
      <form @submit.prevent="login">
        <div class="mb-3">
          <label class="form-label">Usuario</label>
          <input type="text" class="form-control" v-model="username" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Contraseña</label>
          <input type="password" class="form-control" v-model="password" required />
        </div>
        <button type="submit" class="btn btn-primary w-100">Ingresar</button>
      </form>
      <p v-if="error" class="text-danger mt-3">{{ error }}</p>
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
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("http://localhost:5000/login", {
          username: this.username,
          password: this.password,
        });

        // Guardar el token en el LocalStorage
        localStorage.setItem("token", response.data.token);
        localStorage.setItem("user", response.data.user);

        // Redirigir al usuario a la página de eventos
        this.$router.push("/eventos");
      } catch (error) {
        this.error = "Usuario o contraseña incorrectos";
      }
    },
  },
};
</script>
