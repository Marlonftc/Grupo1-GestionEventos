FROM mongo:latest
 
WORKDIR /data
 
COPY feedback.json /data/feedback.json
COPY eventos.json /data/eventos.json
 
# Instalar dos2unix y corregir el formato del script antes de ejecutarlo
RUN apt-get update && apt-get install -y dos2unix

COPY init-mongo.sh /docker-entrypoint-initdb.d/init-mongo.sh

# Convertir el script a formato Unix y dar permisos de ejecución
RUN dos2unix /docker-entrypoint-initdb.d/init-mongo.sh && chmod +x /docker-entrypoint-initdb.d/init-mongo.sh

EXPOSE 27017
