from flask import Blueprint, render_template, request

boletos_bp = Blueprint("boletos", __name__, url_prefix="/boletos")

PRECIO_BOLETO = 12

@boletos_bp.route("/")
def index():
    return render_template("boletos.html")

@boletos_bp.route("/resultado", methods=["POST"])
def resultado():
    nombre = request.form["nombre"]
    cantidad_personas = int(request.form["cantidad_personas"])
    cantidad_boletos = int(request.form["cantidad_boletos"])
    metodo_pago = request.form["metodo_pago"]

    if cantidad_boletos > cantidad_personas * 7:
        return f"Error: No puedes comprar más de {cantidad_personas * 7} boletos."

    subtotal = cantidad_boletos * PRECIO_BOLETO

    descuento = 0
    if cantidad_boletos > 5:
        descuento = 0.15
    elif 3 <= cantidad_boletos <= 5:
        descuento = 0.10

    total = subtotal * (1 - descuento)

    if metodo_pago == "tarjeta":
        total *= 0.90

    return render_template("total.html", nombre=nombre, cantidad_boletos=cantidad_boletos, total=total, cantidad_personas=cantidad_personas)
