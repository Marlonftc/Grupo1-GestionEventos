<template>
  <div class="container mt-5">
    <h1 class="mb-4 text-center">Gestión de Eventos</h1>

    <!-- 🔹 Formulario de creación y edición de eventos -->
    <div class="card p-4 mb-4">
      <h2>{{ editando ? "Editar Evento" : "Crear Nuevo Evento" }}</h2>
      <form @submit.prevent="guardarEvento">
        <div class="mb-3">
          <label class="form-label">Nombre del evento</label>
          <input
            type="text"
            class="form-control"
            v-model="evento.nombre"
            required
          />
        </div>
        <div class="mb-3">
          <label class="form-label">Fecha</label>
          <input
            type="date"
            class="form-control"
            v-model="evento.fecha"
            required
          />
        </div>
        <div class="mb-3">
          <label class="form-label">Ubicación</label>
          <input
            type="text"
            class="form-control"
            v-model="evento.ubicacion"
            required
          />
        </div>
        <div class="mb-3">
          <label class="form-label">Categoría del evento</label>
          <select
            class="form-control"
            v-model="evento.categoria"
            @change="actualizarTiposEventos"
            required
          >
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
            <option v-for="tipo in tiposEventos" :key="tipo" :value="tipo">
              {{ tipo }}
            </option>
          </select>
        </div>

        <button type="submit" class="btn btn-success">
          {{ editando ? "Actualizar" : "Guardar" }}
        </button>
        <button
          type="button"
          class="btn btn-secondary ms-2"
          v-if="editando"
          @click="cancelarEdicion"
        >
          Cancelar
        </button>
      </form>
    </div>
    <div class="card p-4 mb-4">
      <div class="d-flex justify-content-between align-items-center">
        <h2>Lista de Eventos</h2>
        <button class="btn btn-info" @click="cargarEventos">
          Cargar Eventos
        </button>
      </div>

      <ul class="list-group">
        <li
          v-for="ev in eventos"
          :key="ev.id_evento"
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          <!-- Contenido alineado a la izquierda -->
          <div>
            <strong>{{ ev.nombre }}</strong> - {{ ev.fecha }} en
            {{ ev.ubicacion }}
          </div>

          <!-- Botones alineados a la derecha -->
          <div>
            <button class="btn btn-warning mx-2" @click="editarEvento(ev)">
              Editar
            </button>
            <button
              class="btn btn-danger"
              @click="eliminarEvento(ev.id_evento)"
            >
              Eliminar
            </button>
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
      tiposEventos: [], // Lista dinámica de tipos de eventos
      tiposPorCategoria: {
        social: [
          "boda",
          "cumpleaños",
          "graduación",
          "aniversario",
          "baby shower",
          "despedida de soltero",
          "fiesta de quinceañera",
          "reunión familiar",
        ],
        academico: [
          "conferencia",
          "seminario",
          "taller",
          "simposio",
          "coloquio",
          "mesa redonda",
          "defensa de tesis",
          "congreso",
          "charla magistral",
        ],
        deportivo: [
          "maratón",
          "torneo",
          "competencia atlética",
          "carrera ciclística",
          "partido de exhibición",
          "juegos intercolegiales",
          "campeonato nacional",
          "competencia de natación",
          "evento de crossfit",
        ],
      },
    };
  },
  methods: {
    actualizarTiposEventos() {
      this.tiposEventos = this.tiposPorCategoria[this.evento.categoria] || [];
      this.evento.tipo = ""; // Restablecer tipo cuando cambia la categoría
    },
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
        let eventoLimpio = JSON.parse(JSON.stringify(this.evento)); // Convertir en objeto plano

        // Eliminar el id_evento antes de enviarlo (solo en creación)
        if (!this.editando) {
          delete eventoLimpio.id_evento;
        }

        console.log("Enviando evento limpio:", eventoLimpio); // Verificar en consola
        if (!this.editando) {
          await axios.post("http://localhost:5000/eventos", eventoLimpio);
        } else {
          eventoLimpio.origen = "sql";
          await axios.put(
            `http://localhost:5000/eventos/${eventoLimpio.id_evento}`,
            eventoLimpio
          );
        }

        alert("Evento guardado exitosamente");
        this.$emit("eventoGuardado");
        this.cancelarEdicion();
      } catch (error) {
        console.error("Error al guardar evento:", error);
        alert("Error al guardar el evento");
      }
    },
    async eliminarEvento(id) {
      try {
        // Encontrar el evento a eliminar para obtener su origen
        const evento = this.eventos.find((e) => e.id_evento === id);
        if (!evento) {
          alert("Evento no encontrado");
          return;
        }

        const origen = evento.origen || "sql"; // Si no tiene origen, asumimos SQL

        await axios.delete(
          `http://localhost:5000/eventos/${id}?origen=${origen}`
        );

        alert(`Evento eliminado de ${origen}`);
        this.cargarEventos();
      } catch (error) {
        console.error("Error al eliminar evento:", error);
        alert("Error al eliminar el evento");
      }
    },
    editarEvento(ev) {
      this.evento = { ...ev };
      this.editando = true;
      this.actualizarTiposEventos(); // Actualizar la lista de tipos al editar
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
};
</script>
