from django.contrib import admin
from django.db import models
from .models import RegistroUsuarios
from django import forms
from .forms import OpacLibroUsuarioForm #, RegistroUsuariosForm 

#from ajax_select.admin import AjaxSelectAdmin 




@admin.register(RegistroUsuarios)
class RegistroUsuariosAdmin(admin.ModelAdmin):
   

  # form = OpacLibroUsuarioForm

  # list_display = ('nombre_apellidos','institucion_id','tipo_usuario','recurso_prestamo_id','tipo_servicio_solicitado','fecha','hora')

   list_display = ('No','fecha','hora','nombre_apellidos','institucion','tipo_usuario','tipo_servicio_solicitado','prestamo_excepcional','recurso_prestamo')

   search_fields =  ['No','fecha','hora','nombre_apellidos','institucion','tipo_usuario','tipo_servicio_solicitado','prestamo_excepcional','recurso_prestamo']

