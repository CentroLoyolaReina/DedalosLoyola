# Para DAL
#
from dal import autocomplete
from .models import OpacInstitucion, OpacLibro,OpacDescriptor, OpacAutor, OpacEditorial, OpacColeccion, OpacUsuario,OpacMaterias, OpacCiudad, OpacCatedra,OpacTesisAutor, OpacMaterias
#

import ipdb

import os

from django.conf import settings 
from django.http.response import HttpResponse

def OpacSearchRoot(_):
    html = open(os.path.join(settings.STATICFILES_DIRS[0],"VueComponents/vue_opac_search.html"))
    return HttpResponse(html)


def OpacResultsRoot(_):
    html = open(os.path.join(settings.STATICFILES_DIRS[0],"VueComponents/Opac/resultados_busqueda.html"))
    return HttpResponse(html)



class OpacDescriptorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacDescriptor.objects.none()

        qs = OpacDescriptor.objects.all()

        if self.q:
            qs = qs.filter(nombre_descriptor__istartswith=self.q).order_by('nombre_descriptor')

        return qs        


class OpacAutorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacAutor.objects.none()

        qs = OpacAutor.objects.all()

        if self.q:
            qs = qs.filter(nombre_autor__istartswith=self.q).order_by('nombre_autor')

        return qs        
    

class OpacAutor2Autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacAutor.objects.none()

        qs = OpacAutor.objects.all()

        if self.q:
            qs = qs.filter(nombre_autor__istartswith=self.q).order_by('nombre_autor')

        return qs        
    

class OpacAutor3Autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacAutor.objects.none()

        qs = OpacAutor.objects.all()

        if self.q:
            qs = qs.filter(nombre_autor__istartswith=self.q).order_by('nombre_autor')

        return qs        
    

class OpacTesisAutorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacTesisAutor.objects.none()

        qs = OpacTesisAutor.objects.all()

        if self.q:
            qs = qs.filter(nombre_autor__istartswith=self.q).order_by('nombre_autor')

        return qs        


    
class OpacEditorialAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacEditorial.objects.none()

        qs = OpacEditorial.objects.all()

        if self.q:
            qs = qs.filter(nombre_editorial__istartswith=self.q)

        return qs        
    


class OpacColeccionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacColeccion.objects.none()

        qs = OpacColeccion.objects.all()

        if self.q:
            qs = qs.filter(nombre_coleccion__istartswith=self.q).order_by('nombre_coleccion')

        return qs        
    
    

class OpacUsuarioAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacUsuario.objects.none()

        qs = OpacUsuario.objects.all()

        if self.q:
            qs = qs.filter(apellidos__istartswith = self.q).order_by('apellidos') 
          

        return qs 






class OpacMateriasAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacMaterias.objects.none()

        qs = OpacMaterias.objects.all()

        if self.q:
            qs = qs.filter(nombre_materia__istartswith=self.q) 
           

        return qs 



class OpacInstitucionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacInstitucion.objects.none()

        qs = OpacInstitucion.objects.all()

        if self.q:
            qs = qs.filter(nombre_institución__istartswith=self.q) 
           

        return qs 


class OpacCiudadAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacCiudad.objects.none()

        qs = OpacCiudad.objects.all()

        if self.q:
            qs = qs.filter(nombre_ciudad__istartswith=self.q) 
           

        return qs 


class OpacCatedraAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return OpacCatedra.objects.none()

        qs = OpacCatedra.objects.all()

        if self.q:
            qs = qs.filter(nombre_catedra__istartswith=self.q) 
           

        return qs 


