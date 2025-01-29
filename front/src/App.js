import React from "react";
import "./App.css";

function App() {
  return (
    <div className="hero">
      <header className="header">
        <h1>🎊 Gestión de Eventos 🎊</h1>
        <p>Organiza eventos inolvidables con nosotros</p>
      </header>

      <section className="event-options">
        <div className="event-card">
          <img src="https://source.unsplash.com/300x200/?wedding" alt="Boda" />
          <h2>Bodas</h2>
          <p>Elige la mejor decoración, música y catering para tu boda perfecta.</p>
          <button>Explorar Opciones</button>
        </div>

        <div className="event-card">
          <img src="https://source.unsplash.com/300x200/?birthday" alt="Cumpleaños" />
          <h2>Cumpleaños</h2>
          <p>Organiza una fiesta increíble con temáticas personalizadas y animación.</p>
          <button>Explorar Opciones</button>
        </div>
      </section>

      <footer className="footer">
        <p>📍 Ubicación: Ciudad, País | ☎ Contacto: +123 456 7890</p>
      </footer>
    </div>
  );
}

export default App;

