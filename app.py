from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

def generar_data():
    now = datetime.now()

    return {
        "equipo_id": "CAM_001",
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "latitud": -9.189 + random.uniform(-0.005, 0.005),
        "longitud": -77.528 + random.uniform(-0.005, 0.005),
        "velocidad": random.randint(0, 80),
        "estado": "OPERATIVO" if random.random() > 0.2 else "INACTIVO"
    }

@app.route("/gps", methods=["GET"])
def gps():
    return jsonify(generar_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)