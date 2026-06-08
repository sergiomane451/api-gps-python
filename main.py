from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import random
from datetime import datetime

app = FastAPI()

# 🔥 aquí se acumula TODO el historial
data_store = []

# -------------------------
# GENERAR DATO CADA 1 MIN
# -------------------------
def generar_dato():
    now = datetime.now()

    dato = {
        "equipo_id": "CAM_001",
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "latitud": -9.189 + random.uniform(-0.005, 0.005),
        "longitud": -77.528 + random.uniform(-0.005, 0.005),
        "velocidad": random.randint(0, 80),
        "estado": "OPERATIVO"
    }

    data_store.append(dato)

    print("Nuevo registro:", dato)

# -------------------------
# API: HISTORIAL COMPLETO
# -------------------------
@app.get("/gps")
def get_gps():
    return data_store

# -------------------------
# API: ÚLTIMO REGISTRO
# -------------------------
@app.get("/gps/latest")
def get_latest():
    return data_store[-1] if data_store else {}

# -------------------------
# INICIO
# -------------------------

# generar primer dato
generar_dato()

# scheduler cada 1 minuto
scheduler = BackgroundScheduler()
scheduler.add_job(generar_dato, "interval", minutes=1)
scheduler.start()