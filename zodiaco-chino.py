from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

zodiaco_chino = [
    {"signo": "Rata", "imagen": "rata.svg"},
    {"signo": "Búfalo", "imagen": "buey.svg"},
    {"signo": "Tigre", "imagen": "tigre.svg"},
    {"signo": "Conejo", "imagen": "conejo.svg"},
    {"signo": "Dragón", "imagen": "dragon.svg"},
    {"signo": "Serpiente", "imagen": "serpiente.svg"},
    {"signo": "Caballo", "imagen": "caballo.svg"},
    {"signo": "Cabra", "imagen": "cabra.svg"},
    {"signo": "Mono", "imagen": "mono.svg"},
    {"signo": "Gallo", "imagen": "gallo.svg"},
    {"signo": "Perro", "imagen": "perro.svg"},
    {"signo": "Cerdo", "imagen": "cerdo.svg"}
]

def obtener_signo_chino(año):
    ciclo_inicial = 1900
    signo_index = (año - ciclo_inicial) % 12
    return zodiaco_chino[signo_index]["signo"], zodiaco_chino[signo_index]["imagen"]

def calcular_edad(dia, mes, año):
    hoy = datetime.today()
    nacimiento = datetime(año, mes, dia)
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

@app.route("/", methods=["GET", "POST"])
def index():
    imagen = ""
    signo = ""
    nombre = ""
    paterno = ""
    materno = ""
    edad = ""

    if request.method == "POST":
        nombre = request.form["nombre"]
        paterno = request.form["Apterno"]
        materno = request.form["Amaterno"]
        dia = int(request.form["dia"])
        mes = int(request.form["mes"])
        año = int(request.form["año"])

        if año >= 1900:
            signo, imagen = obtener_signo_chino(año)
            edad = calcular_edad(dia, mes, año)

    return render_template("zodiaco.html", nombre=nombre, paterno=paterno, materno=materno, edad=edad, signo=signo, imagen=imagen)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
