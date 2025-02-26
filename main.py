from flask import Flask, render_template, request
import forms
from flask import g, flash
from flask_wtf.csrf import CSRFProtect
from zodiaco import zodiaco_bp
from boletos import boletos_bp

app = Flask(__name__)
app.secret_key = "esta es mi clave secreta"
csrf = CSRFProtect(app)

app.register_blueprint(zodiaco_bp)
app.register_blueprint(boletos_bp)

@app.errorhandler(404)
def page_notfound(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.user = "Mario"
    print("before 1")

@app.after_request
def after_request(response):
    print("after 3")
    return response

@app.route("/")
def index():
    nom = "None"
    titulo = "IDGS801"
    lista = ["lista", "juan", "luis"]
    nom = g.user
    print("Index 2 {}".format(g.user))
    return render_template("index.html", titulo=titulo, lista=lista, nom=nom)

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

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    mat = ''
    nom = ''
    ape = ''
    email = ''
    alumno_class = forms.UserForm(request.form)

    if request.method == 'POST' and alumno_class.validate():
        mat = alumno_class.matricula.data
        nom = alumno_class.nombre.data
        ape = alumno_class.apellido.data
        email = alumno_class.correo.data

        mensaje = f'Bienvenido {nom}'
        flash(mensaje)

    return render_template("alumnos.html", form=alumno_class, mat=mat, nom=nom, ape=ape, email=email)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)
