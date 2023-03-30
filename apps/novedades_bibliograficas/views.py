import os
from url_filter.integrations.drf import DjangoFilterBackend
from novedades_bibliograficas.models import Boletin
from django.conf import settings
from django.http.response import HttpResponse

from rest_framework import viewsets
from .serializers import NovBibliograficasSerializer


#def NovBiblioRoot(_):
#    html = open(os.path.join(settings.STATICFILES_DIRS[0],"VueComponents/lista-boletines/nov_bibliograficas.html"))
#    return HttpResponse(html)
                                                                                                                                                    
class BoletinesViewSet(viewsets.ModelViewSet):                                                                                                    
    queryset = Boletin.objects.all()                                                                                                            
    serializer_class = NovBibliograficasSerializer
 
    filter_backends = [DjangoFilterBackend]       
                                                                                                 
    filter_fields = ("nov_boletin_titulo","nov_boletin_autor","nov_boletin_fecha","nov_boletin_categoria","tipo_de_boletin_id")  



