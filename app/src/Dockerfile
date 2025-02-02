# 🔹 Usamos la imagen oficial de Python en su versión más reciente (3.13.1 slim para reducir tamaño)
FROM python:3.13.1-slim  

# 🔹 Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app  

# 🔹 Actualizamos el sistema y agregamos 'curl' (puede ser útil para pruebas dentro del contenedor)
RUN apt-get update && apt-get install -y curl  

# 🔹 Copiamos el archivo de dependencias 'requirements.txt' al contenedor
COPY requirements.txt .  

# 🔹 Instalamos las dependencias del proyecto sin almacenar caché para reducir el tamaño de la imagen
RUN pip install --no-cache-dir -r requirements.txt  

# 🔹 Copiamos el resto del código al contenedor
COPY . .  

# 🔹 Definimos el comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]  
