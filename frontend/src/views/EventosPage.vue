<template>
  <div class="container mt-5">
    <h1 class="mb-4 text-center">Gestión de Eventos</h1>

    <div class="card p-4">
      <h2>Crear Nuevo Evento</h2>
      <div class="form-group">
        <label>Nombre del evento</label>
        <input type="text" v-model="evento.nombre" class="form-control" placeholder="Nombre del evento">
      </div>

      <div class="form-group">
        <label>Fecha</label>
        <input type="date" v-model="evento.fecha" class="form-control">
      </div>

      <div class="form-group">
        <label>Ubicación</label>
        <input type="text" v-model="evento.ubicacion" class="form-control" placeholder="Ubicación">
      </div>

      <button class="btn btn-primary mt-3" @click="guardarEvento">Guardar</button>
    </div>

    <h2 class="mt-4">Lista de Eventos</h2>
    <button class="btn btn-info mb-3" @click="cargarEventos">Cargar Eventos</button>

    <ul class="list-group">
      <li v-for="ev in eventos" :key="ev.id_evento" class="list-group-item">
        <strong>{{ ev.nombre }}</strong> - {{ ev.fecha }} en {{ ev.ubicacion }}
        <button class="btn btn-warning mx-2" @click="editarEvento(ev)">Editar</button>
        <button class="btn btn-danger" @click="eliminarEvento(ev.id_evento)">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      evento: { nombre: '', fecha: '', ubicacion: '' },
      eventos: []
    };
  },
  methods: {
    async cargarEventos() {
      try {
        const res = await axios.get("http://localhost:5000/reportes");
        this.eventos = res.data;
      } catch (error) {
        console.error("Error al cargar eventos:", error);
      }
    },
    async guardarEvento() {
      try {
        await axios.post("http://localhost:5000/eventos", this.evento);
        this.cargarEventos();
      } catch (error) {
        console.error("Error al guardar evento:", error);
      }
    },
    async eliminarEvento(id) {
      try {
        await axios.delete(`http://localhost:5000/eventos/${id}`);
        this.cargarEventos();
      } catch (error) {
        console.error("Error al eliminar evento:", error);
      }
    },
    editarEvento(ev) {
      this.evento = { ...ev };
    }
  }
};
</script>

