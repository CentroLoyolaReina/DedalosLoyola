from django_elasticsearch_dsl import DocType, Index, Text, indices, Keyword , fields, Text
from .models import RegistroUsuarios


RegistroUsuariosIndex = Index('registro_usuarios')
RegistroUsuariosIndex.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@RegistroUsuariosIndex.doc_type
class RegistroUsuariosDocument(DocType):

    No = fields.KeywordField()

    institucion = fields.ObjectField(properties={
        'id': fields.IntegerField() , 
       
    })

   # hora = fields.DateField()
    
    tipo_usuario = fields.StringField()       
    

    tipo_servicio_solicitado = fields.StringField() 


    recurso_prestamo = fields.ObjectField(properties={
        'no_registro_entrada': fields.StringField() , 

    })

   # def prepare_libro():
   #     if (OpacLibroDocument.baja = True):
   #         not save

    
    class Meta:
        model = RegistroUsuarios
              
        fields = [

            'nombre_apellidos',
            'prestamo_excepcional',
           
            
        ]
