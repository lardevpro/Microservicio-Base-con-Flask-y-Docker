# 🚀 Microservicio Base con Flask y Docker

Este es un microservicio web ligero desarrollado en **Python** utilizando el framework **Flask**. El proyecto está completamente contenedorizado con **Docker** y orquestado mediante **Docker Compose**, lo que facilita enormemente su despliegue y desarrollo local.

---

## 📋 Índice
- [Características Principales](#-características-principales)
- [Tecnologías Utilizadas](#%EF%B8%8F-tecnologías-utilizadas)
- [Estructura del Proyecto](#%EF%B8%8F-estructura-del-proyecto)
- [Endpoints de la API](#-endpoints-de-la-api)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación y Despliegue](#%EF%B8%8F-instalación-y-despliegue)

---

## ✨ Características Principales
* **Despliegue Inmediato:** Configuración lista para entornos de producción y desarrollo mediante contenedores de Docker.
* **Comprobación de Salud:** Endpoint integrado para monitorear el estado operativo del microservicio.
* **Arquitectura Ligera:** Construido sobre Flask, ideal para arquitecturas orientadas a microservicios.

---

## 🛠️ Tecnologías Utilizadas
* **Framework:** [Flask (Python)](https://palletsprojects.com)
* **Contenedorización:** [Docker](https://docker.com) & [Docker Compose](https://docker.com)

---

## 🏗️ Estructura del Proyecto

El repositorio cuenta con la siguiente estructura de archivos base:

```text
├── app.py             # Lógica principal del microservicio y definición de rutas
├── compose.yaml       # Configuración de Docker Compose para levantar el servicio
├── Dockerfile         # Instrucciones de compilación para la imagen Docker de Flask
└── requirements.txt   # Dependencias de Python (Flask)
```

---

## 🛣️ Endpoints de la API

Una vez que el servicio esté corriendo, puedes interactuar con las siguientes rutas en formato **JSON**:

* **`GET /`** - Ruta raíz de bienvenida.
  * **Respuesta exitosa:** `{"message": "Microservicio Docker funcionando correctamente"}`
* **`GET /health`** - Control de estado (Healthcheck) para sistemas de monitoreo o balanceadores de carga.
  * **Respuesta exitosa:** `{"status": "ok"}`

---

## 📌 Requisitos Previos
Para ejecutar este proyecto necesitas tener instalado en tu sistema:
* [Docker Desktop](https://docker.comproducts/docker-desktop/) (incluye Docker Compose)
* [Python 3.x](https://python.org) *(Opcional, solo si deseas ejecutarlo de forma nativa sin usar contenedores)*

---

## ⚙️ Instalación y Despliegue

### Opción A: Despliegue con Docker (Recomendado)

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com
   cd tu-proyecto-flask
   ```

2. **Construye y levanta el contenedor:**
   ```bash
   docker compose up -d --build
   ```

3. **Accede a la aplicación:**
   Abre tu navegador o cliente API (Postman/Insomnia) e ingresa a: **`http://localhost:5000`**

4. **Detener el servicio:**
   ```bash
   docker compose down
   ```

### Opción B: Ejecución Local Tradicional

1. **Crea e inicia un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

2. **Instala las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```
   El servidor comenzará a escuchar en **`http://localhost:5000`**.
