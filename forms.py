from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message="El campo es requerido"),
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
    ])
    apellido=StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido"),
    ])
    correo=EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido"),
    ])

class ZodiacoForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
    ])
    paterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido"),
    ])
    materno = StringField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido"),
    ])
    dia = IntegerField("Día de Nacimiento", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=31, message="Debe estar entre 1 y 31"),
    ])
    mes = IntegerField("Mes de Nacimiento", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=12, message="Debe estar entre 1 y 12"),
    ])
    anio = IntegerField("Año de Nacimiento", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1900, message="Debe ser mayor o igual a 1900"),
    ])
    sexo = RadioField("Sexo", choices=[("masculino", "Masculino"), ("femenino", "Femenino"), ("otro", "Otro")], 
                      validators=[validators.DataRequired(message="Debe seleccionar un sexo")])

    
