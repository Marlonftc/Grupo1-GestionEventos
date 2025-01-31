<template>
  <div class="container mt-5">
    <h1 class="mb-4">Reportes de Eventos Combinados</h1>
    <button class="btn btn-primary" @click="cargarReporte">Generar Reporte</button>

    <div v-if="reporte && reporte.length > 0" class="mt-4">
      <div v-for="evento in reporte" :key="evento.id_evento" class="card mb-3 p-3">
        <h4>{{ evento.nombre }} - {{ evento.fecha }}</h4>
        <p><strong>Ubicación:</strong> {{ evento.ubicacion }}</p>
        <p><strong>Asistentes:</strong> {{ evento.asistentes.length }}</p>
        <p><strong>Servicios:</strong> {{ evento.servicios.length > 0 ? evento.servicios.join(', ') : 'Ninguno' }}</p>
        <p><strong>Presupuesto:</strong> ${{ evento.presupuesto }}</p>
      </div>
    </div>

    <p v-else class="mt-3">No hay reportes disponibles.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      reporte: []  // 🔹 Se inicializa vacío para evitar errores
    };
  },
  methods: {
    async cargarReporte() {
      try {
        const response = await axios.get("http://localhost:5000/reportes");
        this.reporte = response.data;
      } catch (error) {
        console.error("Error al cargar reportes:", error);
        alert("Error al obtener reportes");
      }
    }
  }
};
</script>
