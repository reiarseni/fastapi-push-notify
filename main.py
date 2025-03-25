import asyncio
import json
import uuid
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pywebpush import webpush, WebPushException
from pydantic_settings import BaseSettings


# Configuración de variables de entorno con Pydantic
class Settings(BaseSettings):
    vapid_subject: str
    vapid_public_key: str
    vapid_private_key: str

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI()

# Configurar CORS (ajuste orígenes según necesidad)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta estática para servir sw.js, logo.png, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuración de plantillas Jinja2
templates = Jinja2Templates(directory="templates")

# Acceso a las claves VAPID desde settings
VAPID_SUBJECT = settings.vapid_subject
VAPID_PUBLIC_KEY = settings.vapid_public_key
VAPID_PRIVATE_KEY = settings.vapid_private_key
VAPID_CLAIMS = {"sub": VAPID_SUBJECT}

# Lista global para almacenar las suscripciones (en producción use una BD)
subscriptions = []

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    """
    Sirve la plantilla index.html y pasa la clave pública VAPID para el frontend.
    """
    return templates.TemplateResponse("index.html", {"request": request, "vapid_public_key": VAPID_PUBLIC_KEY})

@app.post("/subscribe")
async def subscribe(request: Request):
    """
    Recibe la suscripción desde el cliente y la almacena.
    """
    sub = await request.json()
    subscriptions.append(sub)
    return JSONResponse({"status": "subscribed"})

async def send_push_notifications():
    """
    Envía una notificación cada 12 segundos a todas las suscripciones registradas.
    """
    while True:
        payload = json.dumps({
            "title": "Notificación",
            "body": f"Notificación de mi sitio remoto./n Tiene nuevos eventos importantes sin leer."
        })
        for sub in subscriptions:
            try:
                webpush(
                    subscription_info=sub,
                    data=payload,
                    vapid_private_key=VAPID_PRIVATE_KEY,
                    vapid_claims=VAPID_CLAIMS
                )
            except WebPushException as ex:
                print("Error al enviar push:", repr(ex))
        await asyncio.sleep(12)

@app.on_event("startup")
async def startup_event():
    # Inicia la tarea en background para enviar notificaciones cada 12 segundos
    asyncio.create_task(send_push_notifications())

