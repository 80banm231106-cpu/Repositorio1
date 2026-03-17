# FROM indica la imagen base que utilizará el contenedor.
# En este caso se utiliza una imagen que ya tiene Python 3.10 instalado.
FROM python:3.10

# WORKDIR establece el directorio de trabajo dentro del contenedor.
# Todos los archivos y comandos se ejecutarán dentro de la carpeta /app.
WORKDIR /app

# COPY copia todos los archivos del proyecto desde la computadora
# hacia el contenedor en el directorio de trabajo.
COPY . .

# CMD define el comando que se ejecutará cuando el contenedor se inicie.
# Aquí se ejecuta el archivo app.py usando Python.
CMD ["python", "app.py"]