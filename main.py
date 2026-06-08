from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import random
from datetime import datetime

app = FastAPI()

# 🔥 último dato generado
latest_data = {}

# -------------------------
# GENERAR DATO NUEVO
# -------------------------
def generar_dato():
    global latest_data

    now = datetime.now()

    latest_data = {
        "equipo_id": "CAM_001",
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "latitud": -9.189 + random.uniform(-0.005, 0.005),
        "longitud": -77.528 + random.uniform(-0.005, 0.005),
        "velocidad": random.randint(0, 80),
        "estado": "OPERATIVO"
    }

    print("Nuevo dato generado:", latest_data)

# -------------------------
# API
# -------------------------
@app.get("/gps")
def get_gps():
    return latest_data

@app.get("/")
def home():
    return {
        "status": "ok",
        "endpoint": "/gps"
    }

# -------------------------
# INICIO
# -------------------------

# generar primer dato al iniciar
generar_dato()

# scheduler cada 1 minuto
scheduler = BackgroundScheduler()
scheduler.add_job(generar_dato, "interval", minutes=1)
scheduler.start()