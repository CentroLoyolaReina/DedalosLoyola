#from django.shortcuts import render

from dal import autocomplete
from opac.models import OpacLibro, OpacUsuario, OpacDescriptor
from .models import RegistroUsuarios


#class RegUsuariosAutocomplete(autocomplete.Select2QuerySetView):
#    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
#        if not self.request.user.is_authenticated():
#            return OpacUsuario.objects.none()

#        qs = OpacUsuario.objects.all()

#        if self.q:
#            qs = qs.filter(nombre__istartswith=self.q)

#        return qs


class RegUsuariosAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return RegistroUsuarios.objects.none()

        qs = RegistroUsuarios.objects.all()

        if self.q:
            qs = qs.filter(nombre_apellidos__istartswith=self.q)

        return qs        

class OpacLibroAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacLibro.objects.none()

        qs = OpacLibro.objects.all()

        if self.q:
            qs = qs.filter(titulo__istartswith=self.q)

        return qs        

class OpacDescriptorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacDescriptor.objects.none()

        qs = OpacDescriptor.objects.all()

        if self.q:
            qs = qs.filter(nombre_descriptor__istartswith=self.q)

        return qs

    
