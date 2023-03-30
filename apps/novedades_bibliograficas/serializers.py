from .models import Boletin
from rest_framework  import serializers



class NovBibliograficasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletin
        fields = ("id","nov_boletin_titulo","nov_boletin_autor","nov_boletin_text","documento_de_boletin","nov_boletin_fecha","nov_boletin_categoria","imagen_de_cubierta","tipo_boletin") 
