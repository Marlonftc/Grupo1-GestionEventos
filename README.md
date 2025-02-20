# 🎉 Gestión de Eventos 📅

Este es un sistema de gestión de eventos que utiliza **Flask**, **Vue.js**, **SQL Server** y **MongoDB**. Permite **crear, editar, eliminar y listar eventos** en diferentes bases de datos, implementando el **patrón Abstract Factory** y arquitecturas flexibles para soportar múltiples tipos de eventos.

---

## 🚀 Características

✅ API en **Flask** con soporte para **SQL Server** y **MongoDB**  
✅ Arquitectura basada en **Abstract Factory**  
✅ CRUD completo de eventos  
✅ Reportes combinados desde SQL y MongoDB  
✅ Integración con **Vue.js** en el frontend  
✅ Documentación con **Swagger**  


## 🛠 **Instalación y Configuración**
### **1️. Requisitos**
- **Docker** y **Docker Compose** (con `WSL 2. Ubuntu como default`)
- **Python 3.9+**
- **Node.js + Vue.js**
- **SQL Server y MongoDB**
- Disponibilidad en los puertos: `7000`, `7001`, `7002`, `7003`, `7004`, `5000`, `27018`, y `1433`

### **2️. Clonar el Repositorio**
```bash
git clone https://github.com/Marlonftc/Grupo1-GestionEventos.git
```

```bash
cd Grupo1-GestionEventos
```

### **3. Configurar y Levantar los Contenedores de Bases de datos**
```bash
docker-compose up --build -d
```

Esto iniciará:

- 📦 **MongoDB**
- 📦 **SQL Server**

Para realizar el respaldo de la base de datos ejecutamos el siguiente comando:
Usando `Powershell` en windows, o bash en linux

```bash
docker exec -i sqlserver /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P 'Mftc@2412' -i /SQLQuery.sql -C
```

### **4. Configurar y Levantar los Contenedores de Back y Frontend**

```bash
docker-compose -f docker-compose-post.yml up --build -d
```
Esto iniciará:

- 📦 **Frontend Vue.js** en `http://localhost:8081` Ctrl + Click
- 📦 **API Flask** en `http://localhost:5000`


---

## 🔥 **Rutas de la API**
### 📝 **Eventos**
| Método | Ruta                | Descripción                              |
|--------|---------------------|------------------------------------------|
| `POST` | `/eventos`          | Crear un nuevo evento                   |
| `PUT`  | `/eventos/{id}`     | Editar un evento                        |
| `DELETE` | `/eventos/{id}`   | Eliminar un evento                      |
| `GET`  | `/reportes`         | Obtener reportes combinados de eventos  |

### 🏗 **Ejemplo de Creación de Evento**
```json
{
  "categoria": "social",
  "tipo": "boda",
  "nombre": "Boda de Ana",
  "fecha": "2025-03-15",
  "ubicacion": "Quito",
  "origen": "sql"
}
```

---

## 🖥 **Frontend (Vue.js)**
Para levantar el frontend manualmente:

```bash
cd frontend
npm install
npm run serv
```
La aplicación estará disponible en 🔗 [http://localhost:8081](http://localhost:8081) Ctrl + Click

---

## 📖 **Swagger API Docs**
Puedes visualizar la documentación de la API en:
🔗 [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

