from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import random
from datetime import datetime
import os

app = Flask(__name__)

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

    print("Dato actualizado:", latest_data)

@app.route("/gps", methods=["GET"])
def gps():
    return jsonify(latest_data)

# 🔄 Scheduler cada 1 minuto
scheduler = BackgroundScheduler()
scheduler.add_job(generar_dato, "interval", minutes=1)
scheduler.start()

# primer dato al iniciar
generar_dato()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)