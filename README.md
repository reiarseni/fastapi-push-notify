# FastAPI Push Notify 🔔

Sistema de envío de notificaciones push a navegadores web usando FastAPI, Service Workers y la API de Notificaciones Web, util para enviar notificaciones en tiempo real a usuarios. Con fines demostrativos el sistema envia una notificacion cada 12 segundos a todos los subscritores. Se ha probado satisfactoriamente en los navegadores Chrome y Firefox.

## 🚀 Características  

- Notificaciones push en tiempo real  
- Soporte para navegadores modernos  
- Manejo de tokens VAPID

## 🛠️ Tecnologías  

- FastAPI  
- Service Workers
- Web Push API
- Pydantic

## 📋 Prerrequisitos  

```bash
python >= 3.8
```

## 🔧 Instalación  

### Clonar el repositorio  

```bash
git clone https://github.com/reiarseni/fastapi-push-notify.git
cd fastapi-push-notify
```

### Crear entorno virtual  

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Instalar dependencias  

```bash
pip install -r requirements.txt
```

### Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

## 🚀 Inicio Rápido  

### Generar claves VAPID

1. Visita [https://vapidkeys.com/](https://vapidkeys.com/)  
2. Genera y copia tus claves pública y privada  
3. Añade las claves a tu archivo `.env`  

```bash
VAPID_PUBLIC_KEY=tu_clave_publica
VAPID_PRIVATE_KEY=tu_clave_privada
VAPID_CLAIMS={"sub": "mailto:tu@email.com"}
```

### Iniciar servidor  

```bash
uvicorn app.main:app --reload
```

Visitar [http://localhost:8000](http://localhost:8000)  

## 📄 Licencia  

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para detalles.  
