from fastapi import FastAPI
from pydantic import BaseModel

# Crear la aplicación
app = FastAPI()

# Modelo de datos para recibir información
class Mensaje(BaseModel):
    texto: str
    usuario: str = "anonimo"

# Ruta básica - GET
@app.get("/")
def inicio():
    return {"mensaje": "¡API funcionando correctamente!"}

# Ruta para procesar mensajes - POST
@app.post("/procesar")
def procesar_mensaje(mensaje: Mensaje):
    # Aquí procesarías la lógica de tu asistente
    respuesta = f"Recibí tu mensaje: {mensaje.texto}"
    
    return {
        "usuario": mensaje.usuario,
        "mensaje_original": mensaje.texto,
        "respuesta": respuesta,
        "estado": "procesado"
    }

# Ruta para el asistente de voz
@app.post("/asistente")
def asistente_voz(mensaje: Mensaje):
    # Lógica específica para el asistente
    texto_usuario = mensaje.texto.lower()
    
    # Ejemplo de lógica simple
    if "hola" in texto_usuario:
        respuesta = "¡Hola! ¿En qué puedo ayudarte?"
    elif "ayuda" in texto_usuario:
        respuesta = "Estoy aquí para asistirte. Pregúntame lo que necesites."
    else:
        respuesta = f"Entiendo que dijiste: {mensaje.texto}"
    
    return {
        "respuesta": respuesta,
        "procesado": True
    }