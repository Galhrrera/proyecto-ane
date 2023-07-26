# # Usa la imagen base de Python
# FROM python:3.11

# # Establece el directorio de trabajo dentro del contenedor
# WORKDIR /app

# # Copia los archivos de tu aplicación al contenedor
# COPY . /app

# # Instala las dependencias
# RUN pip install --no-cache-dir -r requirements.txt

# # Expone el puerto en el que se ejecutará la aplicación
# EXPOSE 8050

# # Comando para ejecutar la aplicación cuando el contenedor se inicie
# CMD ["python3", "app.py"]