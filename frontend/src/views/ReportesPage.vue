<template>
  <div class="container mt-5">
    <h1 class="mb-4">Reportes de Eventos Combinados</h1>
    <button class="btn btn-primary" @click="cargarReporte">Generar Reporte</button>

    <div v-if="Object.keys(reporteAgrupado).length > 0" class="mt-4">
      <div v-for="(eventos, categoria) in reporteAgrupado" :key="categoria" class="mb-4">
        <h2 class="text-primary">{{ categoria.toUpperCase() }}</h2>

        <div v-for="evento in eventos" :key="evento.id_evento" class="card mb-3 p-3">
          <h4>{{ evento.nombre }} - {{ evento.fecha }}</h4>
          <p><strong>Ubicación:</strong> {{ evento.ubicacion }}</p>
          <p><strong>Asistentes:</strong> {{ evento.asistentes }}</p>
          <p><strong>Servicios Contratados:</strong> {{ evento.servicios.length > 0 ? evento.servicios.join(', ') : 'Ninguno' }}</p>
          <p><strong>Presupuesto:</strong> ${{ evento.presupuesto }}</p>

          <h5 class="mt-3">Feedbacks:</h5>
          <ul v-if="evento.feedbacks.length > 0">
            <li v-for="feedback in evento.feedbacks" :key="feedback.cliente">
              <strong>{{ feedback.rating }}⭐</strong> - "{{ feedback.comentario }}"
            </li>
          </ul>
          <p v-else>Sin comentarios</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      reporte: [],
    };
  },
  computed: {
    reporteAgrupado() {
      let agrupado = {};
      this.reporte.forEach(evento => {
        const categoria = evento.categoria || "Sin categoría";
        if (!agrupado[categoria]) {
          agrupado[categoria] = [];
        }
        agrupado[categoria].push(evento);
      });
      return agrupado;
    },
  },
  methods: {
    async cargarReporte() {
      try {
        const response = await axios.get("http://localhost:5000/reportes");
        this.reporte = response.data;
      } catch (error) {
        console.error("Error al obtener el reporte:", error);
      }
    },
  },
};
</script>
