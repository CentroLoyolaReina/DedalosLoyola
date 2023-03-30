from django.db import models
from django.utils import timezone
from opac.models import OpacUsuario, OpacInstitucion, OpacLibro, OpacDescriptor

from multiselectfield import MultiSelectField

class RegistroUsuarios(models.Model):

    LECTURA_EN_SALA =  "Lectura en Sala"
    BUSQUEDA_DE_REFERNCIA =  "Busqueda de Referencia"
    COMPILACION_DE_INFORMACION =  "Compilación de Información"
    REPROGRAFIA = "Reprografía"
    BUSQUEDA_DIGITAL = "Busqueda Digital"
    DOCUMENTOS_DIGITALES = "Busqueda de Documentos Digitales"

    TIPO_ACT = ['Lectura en Sala','Compilación de Información','Reporducción','Busqueda Digital','Busqeuda de Documentos Digitales']

    ESTUDIANTE = "ESTD"
    PROFESOR = "PROF"
    INVESTIGADOR = "INVEST"
    TRABAJADOR = "TRABAJ"
    VISITANTE_EXTERNO = "VISTEXT"
    PRESBITERO = "PRESBIT"
    NOVICIO = "NOVICIO"

    
    TIPO_SERV_SOLICITADO = (
            (LECTURA_EN_SALA,"Lectura en Sala"),
            (BUSQUEDA_DE_REFERNCIA,"Busqueda de Referencia"),
            (COMPILACION_DE_INFORMACION,"Compilación de Información"),
            (BUSQUEDA_DIGITAL,"Busqueda Digital"),
            (REPROGRAFIA,"Reprografía"),
            (DOCUMENTOS_DIGITALES,"Documentos Digitales"),
    
    )

    TIPO_USUARIO = (
        (ESTUDIANTE,"Estudiante"),
        (NOVICIO,"Novicio"),
        (PROFESOR,"Profesor"),
        (INVESTIGADOR,"Investigador"),
        (PRESBITERO,"Presbitero"),
        (TRABAJADOR,"Trabajador"),
        (VISITANTE_EXTERNO,"Visitante Externo a la Institución"),
    )
    
    No = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add = False,default="1970-01-01")
    hora = models.TimeField(auto_now_add = False, default="01:01:00")
    nombre_apellidos = models.CharField(max_length=90, default=" ")
    #posee_carnet = models.NullBooleanField(default=False)
    #ncb = models.CharField(max_length=11, null=True, blank=True)
    institucion = models.ForeignKey(OpacInstitucion,default=1)
    tipo_usuario = models.CharField(max_length=15, choices=TIPO_USUARIO, default=NOVICIO)
    tipo_servicio_solicitado = MultiSelectField(max_length=120,choices=(TIPO_SERV_SOLICITADO),default='Lectura en Sala')
    prestamo_excepcional = models.BooleanField(default=False)
    recurso_prestamo = models.ForeignKey(OpacLibro, null=True, blank=True)
    
    
    
    class Meta:
        managed = True
        db_table = 'reg_usuarios'
        verbose_name = 'Usuario Presencial'
        verbose_name_plural = 'Registro de Usuarios Presenciales'

    def __str__(self):
        return self.nombre_apellidos


