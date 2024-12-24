from django import forms
from django.contrib.auth.forms import AuthenticationForm
from appsena.models import report



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    error_messages = {
        'invalid_login': (
            "Por favor, introduzca un nombre de usuario y una contraseña correctos. "
            "Tenga en cuenta que ambos campos pueden ser sensibles a mayúsculas."
        ),
        'inactive': "Esta cuenta está inactiva.",
    }

class CustomForm(forms.Form):
    campo1 = forms.CharField(label='Campo 1', max_length=100)
    campo2 = forms.CharField(label='Campo 2', max_length=100)
    campo3 = forms.CharField(label='Campo 3', max_length=100)
    campo4 = forms.CharField(label='Campo 4', max_length=100)
    campo5 = forms.CharField(label='Campo 5', max_length=100)
    
   
   
OPCIONES = [
    ('ID', 'ID'),
    ('CÓDIGO_REGIONAL', 'CÓDIGO REGIONAL'),
    ('NOMBRE_REGIONAL', 'NOMBRE REGIONAL'),
    ('CÓDIGO_CENTRO', 'CÓDIGO CENTRO'),
    ('NOMBRE_CENTRO', 'NOMBRE CENTRO'),
    ('CÓDIGO_MESA_SECTORIAL', 'CÓDIGO MESA SECTORIAL'),
    ('NOMBRE_MESA_SECTORIAL', 'NOMBRE MESA SECTORIAL'),
    ('CÓDIGO_NORMA', 'CÓDIGO NORMA'),
    ('VERSIÓN_NORMA', 'VERSIÓN NORMA'),
    ('NOMBRE_NORMA', 'NOMBRE NORMA'),
    ('ID_PROYECTO', 'ID PROYECTO'),
    ('ID_GRUPO', 'ID GRUPO'),
    ('LINEA_ATENCIÓN', 'LINEA ATENCIÓN'),
    ('NIT_EMPRESA', 'NIT EMPRESA'),
    ('NOMBRE_EMPRESA', 'NOMBRE EMPRESA'),
    ('PROYECTO_NACIONAL', 'PROYECTO NACIONAL'),
    ('TIPO_IDENTIFICACIÓN_CANDIDATO', 'TIPO IDENTIFICACIÓN CANDIDATO'),
    ('PAIS_DE_NACIMIENTO', 'PAÍS DE NACIMIENTO'),
    ('DEPARTAMENTO_NACIMIENTO', 'DEPARTAMENTO NACIMIENTO'),
    ('MUNICIPIO_NACIMIENTO', 'MUNICIPIO NACIMIENTO'),
    ('FECHA_NACIMIENTO_CANDIDATO', 'FECHA NACIMIENTO CANDIDATO'),
    ('SEXO_CANDIDATO', 'SEXO CANDIDATO'),
    ('GENERO_CANDIDATO', 'GÉNERO CANDIDATO'),
    ('COMUNIDAD_LGBTI_CANDIDATO', 'COMUNIDAD LGBTI CANDIDATO'),
    ('ESTADO_CIVIL_CANDIDATO', 'ESTADO CIVIL CANDIDATO'),
    ('NIVEL_DE_ESTUDIOS_CANDIDATO', 'NIVEL DE ESTUDIOS CANDIDATO'),
    ('TIPO_POBLACIÓN_CANDIDATO', 'TIPO POBLACIÓN CANDIDATO'),
    ('CONDICIÓN_LABORAL_CANDIDATO', 'CONDICIÓN LABORAL CANDIDATO'),
    ('PAIS_RESIDENCIA_CANDIDATO', 'PAÍS RESIDENCIA CANDIDATO'),
    ('DEPARTAMENTO_RESIDENCIA_CANDIDATO', 'DEPARTAMENTO RESIDENCIA CANDIDATO'),
    ('MUNICIPIO_RESIDENCIA_CANDIDATO', 'MUNICIPIO RESIDENCIA CANDIDATO'),
    ('CÓDIGO_PAIS_RESIDENCIA', 'CÓDIGO PAÍS RESIDENCIA'),
    ('CÓDIGO_MUNICIPIO_RESIDENCIA', 'CÓDIGO MUNICIPIO RESIDENCIA'),
    ('CÓDIGO_DEPARTAMENTO_RESIDENCIA', 'CÓDIGO DEPARTAMENTO RESIDENCIA'),
    ('ESTRATO_CANDIDATO', 'ESTRATO CANDIDATO'),
    ('CONDICION_DE_DISCAPACIDAD', 'CONDICIÓN DE DISCAPACIDAD'),
    ('DISCAPACIDADES_FECHA_CERTIFICACION', 'DISCAPACIDADES FECHA CERTIFICACIÓN'),
    ('TIPO_ID_EVALUADOR', 'TIPO ID EVALUADOR'),
    ('NUMERO_ID_EVALUADOR', 'NÚMERO ID EVALUADOR'),
    ('NOMBRE_EVALUADOR', 'NOMBRE EVALUADOR'),
    ('TIPO_USUARIO_EVALUADOR', 'TIPO USUARIO EVALUADOR'),
    ('TIPO_VINCULACION_EVALUADOR', 'TIPO VINCULACIÓN EVALUADOR'),
    ('NIVEL_CERTIFICADO', 'NIVEL CERTIFICADO'),
    ('VALORACIÓN_CONOCIMIENTO', 'VALORACIÓN CONOCIMIENTO'),
    ('VALORACIÓN_PRODUCTO', 'VALORACIÓN PRODUCTO'),
    ('VALORACIÓN_DESEMPEÑO', 'VALORACIÓN DESEMPEÑO'),
    ('COLOMBIANO_RETORNADO', 'COLOMBIANO RETORNADO'),
    ('POBLACIÓN_DE_ACOGIDA', 'POBLACIÓN DE ACOGIDA'),
    ('EXTENSIONISTA_RURAL', 'EXTENSIONISTA RURAL'),
    ('POBLACIÓN_CAMPESINA', 'POBLACIÓN CAMPESINA'),
    ('TIPO_CERTIFICATON', 'TIPO CERTIFICACIÓN'),
    ('OBSERVACIÓN_CERTIFICATON', 'OBSERVACIÓN CERTIFICACIÓN'),
    ('EDAD', 'EDAD'),
]

OPCIONES2 = [
    ('PERSONAS CERTIFICADAS', 'PERSONAS CERTIFICADAS'),
    ('ECONOMIA POPULAR', 'ECONOMIA POPULAR'),
  
]
class CustomForm(forms.Form):
    
    Reportes = forms.ChoiceField(label='Reportes', choices = OPCIONES2 )
    campo1 = forms.ChoiceField(label='Campo 1', choices=OPCIONES)
    campo2 = forms.ChoiceField(label='Campo 2', choices=OPCIONES)
    campo3 = forms.ChoiceField(label='Campo 3', choices=OPCIONES)
    campo4 = forms.ChoiceField(label='Campo 4', choices=OPCIONES)
    campo5 = forms.ChoiceField(label='Campo 5', choices=OPCIONES)
   