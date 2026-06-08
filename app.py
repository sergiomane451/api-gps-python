from fastapi import FastAPI
import random
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import os

app = FastAPI()

latest_data = {}

def generar_dato():
    global latest_data

    now = datetime.now()

    latest_data = {
        "equipo_id": "CAM_001",
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "latitud": -9.189 + random.uniform(-0.005, 0.005),
        "longitud": -77.528 + random.uniform(-0.005, 0.005),
        "velocidad": random.randint(0, 80),
        "estado": "OPERATIVO" if random.random() > 0.2 else "INACTIVO"
    }

@app.get("/gps")
def gps():
    return latest_data

generar_dato()

scheduler = BackgroundScheduler()
scheduler.add_job(generar_dato, "interval", minutes=1)
scheduler.start()

# 🔥 IMPORTANTE PARA RENDER
port = int(os.environ.get("PORT", 8000))