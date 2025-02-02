# 🔹 Usa la última versión oficial de MongoDB como imagen base
FROM mongo:latest

# 🔹 Establece el directorio de trabajo en /data dentro del contenedor 
WORKDIR /data
 
# 🔹 Copia los archivos JSON de datos iniciales a la carpeta /data dentro del contenedor
COPY feedback.json /data/feedback.json
COPY eventos.json /data/eventos.json
 
# Instalar dos2unix y corregir el formato del script antes de ejecutarlo
RUN apt-get update && apt-get install -y dos2unix

# 🔹 Copia el script de inicialización a la carpeta de entrada de MongoDB
COPY init-mongo.sh /docker-entrypoint-initdb.d/init-mongo.sh

# Convertir el script a formato Unix y dar permisos de ejecución
RUN dos2unix /docker-entrypoint-initdb.d/init-mongo.sh && chmod +x /docker-entrypoint-initdb.d/init-mongo.sh

# 🔹 Expone el puerto 27017 para permitir conexiones externas a la base de datos
EXPOSE 27017
