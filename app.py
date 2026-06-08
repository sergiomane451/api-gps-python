from fastapi import FastAPI
import random
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import os

app = FastAPI()

# 🔥 solo último dato
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

    print("Actualizado:", latest_data)

# 🚀 endpoint
@app.get("/gps")
def get_gps():
    return latest_data

# 🔄 scheduler cada 1 minuto
scheduler = BackgroundScheduler()
scheduler.add_job(generar_dato, "interval", minutes=1)
scheduler.start()

# generar primer dato
generar_dato()