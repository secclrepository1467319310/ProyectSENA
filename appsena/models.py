from django.db import models

# Create your models here.
class report(models.Model):
    CODIGO_REGIONAL = models.CharField(max_length=50)
    NOMBRE_REGIONAL = models.CharField(max_length=100)
    CODIGO_CENTRO = models.CharField(max_length=50)
    NOMBRE_CENTRO = models.CharField(max_length=100)
    CODIGO_MESA_SECTORIAL = models.CharField(max_length=50)
    NOMBRE_MESA_SECTORIAL = models.CharField(max_length=100)
    CODIGO_NORMA = models.CharField(max_length=50)
    VERSION_NORMA = models.CharField(max_length=50)
    NOMBRE_NORMA = models.CharField(max_length=100)
    ID_PROYECTO = models.CharField(max_length=50)
    ID_GRUPO = models.CharField(max_length=50)
    LINEA_ATENCION = models.CharField(max_length=100)
    NIT_EMPRESA = models.CharField(max_length=50)
    NOMBRE_EMPRESA = models.CharField(max_length=100)
    PROYECTO_NACIONAL = models.CharField(max_length=50)
    TIPO_IDENTIFICACION_CANDIDATO = models.CharField(max_length=50)
    PAIS_DE_NACIMIENTO = models.CharField(max_length=50)
    DEPARTAMENTO_NACIMIENTO = models.CharField(max_length=50)
    MUNICIPIO_NACIMIENTO = models.CharField(max_length=50)
    FECHA_NACIMIENTO_CANDIDATO = models.DateField()
    SEXO_CANDIDATO = models.CharField(max_length=10)
    GENERO_CANDIDATO = models.CharField(max_length=10)
    COMUNIDAD_LGBTI_CANDIDATO = models.CharField(max_length=10)
    ESTADO_CIVIL_CANDIDATO = models.CharField(max_length=50)
    NIVEL_DE_ESTUDIOS_CANDIDATO = models.CharField(max_length=50)
    TIPO_POBLACION_CANDIDATO = models.CharField(max_length=50)
    CONDICION_LABORAL_CANDIDATO = models.CharField(max_length=50)
    PAIS_RESIDENCIA_CANDIDATO = models.CharField(max_length=50)
    DEPARTAMENTO_RESIDENCIA_CANDIDATO = models.CharField(max_length=50)
    MUNICIPIO_RESIDENCIA_CANDIDATO = models.CharField(max_length=50)
    CODIGO_PAIS_RESIDENCIA = models.CharField(max_length=50)
    CODIGO_MUNICIPIO_RESIDENCIA = models.CharField(max_length=50)
    CODIGO_DEPARTAMENTO_RESIDENCIA = models.CharField(max_length=50)
    ESTRATO_CANDIDATO = models.CharField(max_length=10)
    CONDICION_DE_DISCAPACIDAD = models.DateField() # TODO
    DISCAPACIDADES = models.CharField(max_length=50)
    FECHA_CERTIFICACION = models.CharField(max_length=50)
    TIPO_ID_EVALUADOR = models.CharField(max_length=50)
    NUMERO_ID_EVALUADOR = models.CharField(max_length=100)
    NOMBRE_EVALUADOR = models.CharField(max_length=50)
    TIPO_USUARIO_EVALUADOR = models.CharField(max_length=50)
    TIPO_VINCULACION_EVALUADOR = models.CharField(max_length=50)
    NIVEL_CERTIFICADO = models.CharField(max_length=50)
    VALORACION_CONOCIMIENTO = models.CharField(max_length=50)
    VALORACION_PRODUCTO = models.CharField(max_length=50)
    VALORACION_DESEMPENIO = models.CharField(max_length=50)
    COLOMBIANO_RETORNADO = models.CharField(max_length=50)
    POBLACION_DE_ACOGIDA = models.CharField(max_length=50)
    EXTENSIONISTA_RURAL = models.CharField(max_length=50)
    POBLACION_CAMPESINA = models.CharField(max_length=50)
    TIPO_CERTIFICATON = models.CharField(max_length=100)
    OBSERVACION_CERTIFICATON = models.CharField(max_length=100)
    EDAD =  models.IntegerField(max_length=10)
    


    


    
 

