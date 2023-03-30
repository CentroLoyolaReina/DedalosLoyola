from django.contrib import admin
from .models import TipoBoletin,Boletin



class TipoBoletinAdmin(admin.ModelAdmin):
    search_display = ('tipo_de_boletin',)
    list_display = ['tipo_de_boletin',]

class BoletinAdmin(admin.ModelAdmin):
    search_display = ('nov_boletin_titulo','nov_boletin_autor','nov_boletin_fecha','nov_boletin_categoria',)
    list_display  = ['nov_boletin_titulo','nov_boletin_autor','nov_boletin_fecha','nov_boletin_categoria',]   


admin.site.register(TipoBoletin,TipoBoletinAdmin)
admin.site.register(Boletin,BoletinAdmin)  
