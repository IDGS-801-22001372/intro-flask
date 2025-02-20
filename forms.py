from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula"[
        validators.DataRequired(message="El campo es requerido")
        validators.lenght(min=3,max=10, message="3-10 caracteres")
    ])
    nombre=StringField("Nombre")
    apellido=StringField("Apellido")
    correo=EmailField("Correo")