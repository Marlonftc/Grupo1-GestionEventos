<template>
  <div class="container mt-5">
    <h1 class="mb-4 text-center">Gestión de Eventos</h1>

    <!-- 🔹 Formulario de creación y edición de eventos -->
    <div class="card p-4 mb-4">
      <h2>{{ editando ? "Editar Evento" : "Crear Nuevo Evento" }}</h2>
      <form @submit.prevent="guardarEvento">
        <div class="mb-3">
          <label class="form-label">Nombre del evento</label>
          <input type="text" class="form-control" v-model="evento.nombre" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Fecha</label>
          <input type="date" class="form-control" v-model="evento.fecha" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Ubicación</label>
          <input type="text" class="form-control" v-model="evento.ubicacion" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Categoría del evento</label>
          <select class="form-control" v-model="evento.categoria" @change="actualizarTiposEventos" required>
            <option value="">Selecciona una categoría</option>
            <option value="social">Social</option>
            <option value="academico">Académico</option>
            <option value="deportivo">Deportivo</option>
          </select>
        </div>
        <div class="mb-3" v-if="evento.categoria">
          <label class="form-label">Tipo de evento</label>
          <select class="form-control" v-model="evento.tipo" required>
            <option value="">Selecciona un tipo</option>
            <option v-for="tipo in tiposEventos" :key="tipo" :value="tipo">{{ tipo }}</option>
          </select>
        </div>

        <button type="submit" class="btn btn-success">
          {{ editando ? "Actualizar" : "Guardar" }}
        </button>
        <button type="button" class="btn btn-secondary ms-2" v-if="editando" @click="cancelarEdicion">
          Cancelar
        </button>
      </form>
    </div>

    <!-- 🔹 Lista de Eventos -->
    <div class="card p-4 mb-4">
      <div class="d-flex justify-content-between align-items-center">
        <h2>Lista de Eventos</h2>
        <button class="btn btn-info" @click="cargarEventos">🔄 Cargar Eventos</button>
      </div>

      <ul class="list-group">
        <li v-for="ev in eventos" :key="ev.id_evento" class="list-group-item d-flex justify-content-between align-items-center">
          <div>
            <strong>{{ ev.nombre }}</strong> - {{ ev.fecha }} en {{ ev.ubicacion }}
          </div>
          <div>
            <button class="btn btn-warning mx-2" @click="editarEvento(ev)">✏️ Editar</button>
            <button class="btn btn-danger" @click="eliminarEvento(ev.id_evento)">🗑️ Eliminar</button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      eventos: [],
      evento: {
        id_evento: null,
        nombre: "",
        fecha: "",
        ubicacion: "",
        tipo: "",
        categoria: "",
        origen: "sql",
      },
      editando: false,
      tiposEventos: [],
      tiposPorCategoria: {
        social: ["boda", "cumpleaños", "graduación", "aniversario"],
        academico: ["conferencia", "seminario", "taller", "simposio"],
        deportivo: ["maratón", "torneo", "competencia atlética"],
      },
      error: null,
    };
  },
  methods: {
    actualizarTiposEventos() {
      this.tiposEventos = this.tiposPorCategoria[this.evento.categoria] || [];
      this.evento.tipo = "";
    },
    
    async cargarEventos() {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          this.error = "⚠️ No estás autenticado. Inicia sesión.";
          return;
        }

        const res = await axios.get("http://localhost:5000/reportes", {
          headers: { Authorization: `Bearer ${token}` },
        });

        this.eventos = res.data;
      } catch (error) {
        console.error("Error al cargar eventos:", error);
        this.error = "⚠️ No tienes permiso para ver los eventos o tu sesión expiró.";
      }
    },

    async guardarEvento() {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          alert("⚠️ No estás autenticado. Inicia sesión.");
          return;
        }

        let eventoLimpio = JSON.parse(JSON.stringify(this.evento));

        if (!this.editando) {
          delete eventoLimpio.id_evento;
        }

        console.log("Enviando evento limpio:", eventoLimpio);

        if (!this.editando) {
          await axios.post("http://localhost:5000/eventos", eventoLimpio, {
            headers: { Authorization: `Bearer ${token}` },
          });
        } else {
          eventoLimpio.origen = "sql";
          await axios.put(`http://localhost:5000/eventos/${eventoLimpio.id_evento}`, eventoLimpio, {
            headers: { Authorization: `Bearer ${token}` },
          });
        }

        alert("✅ Evento guardado exitosamente");
        this.cancelarEdicion();
        this.cargarEventos();
      } catch (error) {
        console.error("Error al guardar evento:", error);
        alert("⚠️ No tienes permisos para esta acción o tu sesión expiró.");
      }
    },

    async eliminarEvento(id) {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          alert("⚠️ No estás autenticado. Inicia sesión.");
          return;
        }

        const evento = this.eventos.find((e) => e.id_evento === id);
        if (!evento) {
          alert("⚠️ Evento no encontrado.");
          return;
        }

        const origen = evento.origen || "sql";

        await axios.delete(`http://localhost:5000/eventos/${id}?origen=${origen}`, {
          headers: { Authorization: `Bearer ${token}` },
        });

        alert(`✅ Evento eliminado de ${origen}`);
        this.cargarEventos();
      } catch (error) {
        console.error("Error al eliminar evento:", error);
        alert("⚠️ No tienes permisos para eliminar este evento o tu sesión expiró.");
      }
    },

    editarEvento(ev) {
      this.evento = { ...ev };
      this.editando = true;
      this.actualizarTiposEventos();
    },

    cancelarEdicion() {
      this.evento = {
        id_evento: null,
        nombre: "",
        fecha: "",
        ubicacion: "",
        tipo: "",
        categoria: "",
        origen: "sql",
      };
      this.editando = false;
    },
  },
  mounted() {
    this.cargarEventos();
  },
};
</script>
