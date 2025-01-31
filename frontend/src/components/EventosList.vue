<template>
  <div class="container mt-4">
    <h2>Lista de Eventos</h2>
    <button class="btn btn-primary mb-3" @click="cargarEventos">Cargar Eventos</button>

    <ul class="list-group">
      <li v-for="evento in eventos" :key="evento.id_evento" class="list-group-item d-flex justify-content-between align-items-center">
        <div>
          <strong>{{ evento.nombre }}</strong> - {{ evento.fecha }} en {{ evento.ubicacion }}
        </div>
        <div>
          <button class="btn btn-warning btn-sm me-2" @click="editarEvento(evento)">Editar</button>
          <button class="btn btn-danger btn-sm" @click="eliminarEvento(evento.id_evento)">Eliminar</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      eventos: []
    };
  },
  methods: {
    async cargarEventos() {
      try {
        const response = await axios.get("http://localhost:5000/reportes");
        this.eventos = response.data;
      } catch (error) {
        console.error("Error al obtener eventos:", error);
      }
    },
    async eliminarEvento(id) {
      if (!confirm("¿Estás seguro de eliminar este evento?")) return;
      try {
        await axios.delete(`http://localhost:5000/eventos/${id}`);
        this.cargarEventos();
        alert("Evento eliminado correctamente");
      } catch (error) {
        console.error("Error al eliminar evento:", error);
        alert("Error al eliminar el evento");
      }
    },
    editarEvento(evento) {
      this.$emit("editar", evento);
    }
  }
};
</script>

