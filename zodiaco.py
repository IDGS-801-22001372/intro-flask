from flask import Blueprint, render_template, request
from datetime import datetime
from flask import g, flash
import forms


zodiaco_bp = Blueprint("zodiaco", __name__, url_prefix="")

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

@zodiaco_bp.route("/zodiaco", methods=["GET", "POST"])
def index():
    form = forms.ZodiacoForm(request.form)
    signo = ""
    imagen = ""
    edad = ""
    sexo = ""
    nombre = ""
    paterno = ""
    materno = ""

    if request.method == "POST" and form.validate():
        nombre = form.nombre.data
        paterno = form.paterno.data
        materno = form.materno.data
        dia = form.dia.data
        mes = form.mes.data
        anio = form.anio.data
        sexo = form.sexo.data.capitalize()
        signo, imagen = obtener_signo_chino(anio)
        edad = calcular_edad(dia, mes, anio)

        mensaje = f"{nombre} {paterno} {materno}, tu signo es {signo}, tienes {edad} años y tu sexo es {sexo}."
        flash(mensaje)
    elif request.method == "GET":
        form = forms.ZodiacoForm()

    return render_template("zodiaco.html", form=form, signo=signo, imagen=imagen, edad=edad, sexo=sexo,
                           nombre=nombre, paterno=paterno, materno=materno)
