# FastAPI Push Notify 🔔

Sistema de demostracion de uso de notificaciones push para navegadores web usando FastAPI, Service Workers y la API de Notificaciones Web, util para enviar notificaciones en tiempo real a usuarios.Aquí tienes la versión corregida en formato Markdown:

## 🚀 Características  

- Notificaciones push en tiempo real  
- Soporte para navegadores modernos  
- Manejo de tokens VAPID

## 🛠️ Tecnologías  

- FastAPI  
- Service Workers  
- Web Push API  
- SQLite  
- Vue.js  
- Pydantic  
- WebSocket (opcional)  

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

Visitar [http://localhost:8000/docs](http://localhost:8000/docs)  


## 🔐 Seguridad  

- Implementación completa de VAPID  
- Validación de tokens  
- Rate limiting  
- CORS configurado  
- Headers de seguridad  

## 🤝 Contribuir  

1. Fork el proyecto  
2. Crear una rama (`git checkout -b feature/AmazingFeature`)  
3. Commit cambios (`git commit -m 'Add: nueva característica'`)  
4. Push a la rama (`git push origin feature/AmazingFeature`)  
5. Abrir Pull Request  

## 📄 Licencia  

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para detalles.  
