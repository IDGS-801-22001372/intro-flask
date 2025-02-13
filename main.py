from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "IDGS801"
    lista = ["lista", "juan", "luis"]
    return render_template("index.html", titulo=titulo)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/hola")
def hola():
    return "<h1>Hola, Mundo!</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1>Hola, {user}!</h1>"

@app.route("/numero/<int:numero>")
def number(numero):
    return f"<h1>El numero es {numero}!</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>Hola, {username}! Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola, {param}</h1>"

@app.route("/operas")
def operas():
    return '''
    <form action="">
        <label for="">Name</label>
        <input type="text" id="name" name="name" required>

        <label for="">APaterno</label>
        <input type="text" id="APaterno" name="APaterno" required>
    </form>
           '''

@app.route("/opera-bas")
def operas1():
    print("Accediendo a /opera-bas")
    return render_template("opera-bas.html")

@app.route("/resultado", methods=["POST"])
def result():
    try:
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = n1 + n2
            op_texto = "suma"
        elif operacion == "resta":
            resultado = n1 - n2
            op_texto = "resta"
        elif operacion == "multiplicacion":
            resultado = n1 * n2
            op_texto = "multiplicación"
        elif operacion == "division":
            if n2 == 0:
                return "Error: No se puede dividir por cero."
            resultado = n1 / n2
            op_texto = "división"
        else:
            return "Operación no válida."

        return f"La {op_texto} de {n1} y {n2} es: {resultado}"

    except ValueError:
        return "Error: Ingresa valores numéricos válidos."

if __name__ == "__main__":
    app.run(debug=True, port=3000)