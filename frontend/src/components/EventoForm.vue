<template>
  <div class="card p-4 mb-4">
    <h2>{{ editando ? 'Editar Evento' : 'Crear Nuevo Evento' }}</h2>
    <form @submit.prevent="guardarEvento">
      <div class="mb-3">
        <label class="form-label">Nombre del evento</label>
        <input type="text" class="form-control" v-model="evento.nombre" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Fecha</label>
        <input type="date" class="form-control" v-model="evento.fecha" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Ubicación</label>
        <input type="text" class="form-control" v-model="evento.ubicacion" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Tipo de evento</label>
        <select class="form-control" v-model="evento.tipo">
          <option value="boda">Boda</option>
          <option value="cumpleaños">Cumpleaños</option>
          <option value="conferencia">Conferencia</option>
        </select>
      </div>
      <button type="submit" class="btn btn-success">{{ editando ? 'Actualizar' : 'Guardar' }}</button>
      <button type="button" class="btn btn-secondary ms-2" v-if="editando" @click="cancelarEdicion">Cancelar</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["eventoEditar"],
  data() {
    return {
      evento: { id_evento: null, nombre: "", fecha: "", ubicacion: "", tipo: "boda" },
      editando: false
    };
  },
  watch: {
    eventoEditar(nuevoEvento) {
      if (nuevoEvento) {
        this.evento = { ...nuevoEvento };
        this.editando = true;
      }
    }
  },
  methods: {
    async guardarEvento() {
      try {
        await axios.post("http://localhost:5000/eventos", this.evento);
        alert("Evento guardado exitosamente");
        this.$emit("eventoGuardado");
      } catch (error) {
        console.error("Error al guardar evento:", error);
        alert("Error al guardar el evento");
      }
    },
    cancelarEdicion() {
      this.evento = { id_evento: null, nombre: "", fecha: "", ubicacion: "", tipo: "boda" };
      this.editando = false;
      this.$emit("cancelar");
    }
  }
};
</script>



