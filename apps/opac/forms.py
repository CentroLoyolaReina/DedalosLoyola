from django import forms
from dal import autocomplete
from .models import OpacInstitucion, OpacLibro, OpacDescriptor,  OpacAutor, OpacEditorial, OpacColeccion,OpacCiudad, OpacCatedra, OpacTesisAutor, OpacMaterias


INDICES_DE_BUSQUEDA = (
    ('libros','Libros'),
    ('revistas','Revistas'),
    ('tesis','Tesis'),
)

#import ipdb ; ipdb.set_trace()
class FormularioBusqueda(forms.Form):
    termino_de_busqueda = forms.CharField()
    opcion_de_busqueda = forms.ChoiceField(choices=INDICES_DE_BUSQUEDA)

class LibroForm(forms.ModelForm):


    descriptores = forms.ModelMultipleChoiceField(
        queryset = OpacDescriptor.objects.all(),
        widget = autocomplete.ModelSelect2Multiple(url='opac-descriptor-autocomplete')
        )
    
    autor = forms.ModelChoiceField(
            queryset = OpacAutor.objects.all(),
            widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete')
            ) 

    autor2 = forms.ModelChoiceField(
            queryset = OpacAutor.objects.all(),
            widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete'),
            required=False
            )
          
    autor3 = forms.ModelChoiceField(
            queryset = OpacAutor.objects.all(),
            widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete'),
            required=False
            )
                
#===========Borre estos dos campos de autocompletamiento porque salian dobles al final del listado de libros    
#    casa_editora = forms.ModelChoiceField(
#        queryset = OpacEditorial.objects.all(),
#        widget = autocomplete.ModelSelect2(url='opac-editorial-autocomplete')
#        )
          
#    colección = forms.ModelChoiceField(
#        queryset = OpacColeccion.objects.all(),
#        widget = autocomplete.ModelSelect2(url='opac-coleccion-autocomplete'),
#        required=False

#        )

        

    lugar_de_edición = forms.ModelChoiceField(
        queryset = OpacCiudad.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-ciudad-autocomplete'),
        required=False
        )    

   
    
    
#class RevistaEjemplarForm(forms.ModelForm):

   
#    editorial = forms.ModelChoiceField(
#        queryset = OpacEditorial.objects.all(),
#        widget = autocomplete.ModelSelect2(url='opac-editorial-autocomplete')
#        )
    
    

#    institución = forms.ModelChoiceField(
#            queryset = OpacInstitucion.objects.all(),
#            widget = autocomplete.ModelSelect2(url='opac-institucion-autocomplete'),
#            required=False
#    )
    
#    nombre_materia = forms.ModelChoiceField(
#        queryset = OpacMaterias.objects.all(),
#        widget = autocomplete.ModelSelect2(url='opac-materias-autocomplete')
#    )


#class RevistaArticuloForm(forms.ModelForm):
#    autor = forms.ModelChoiceField(
#        queryset = OpacAutor.objects.all(),
#        widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete')
#        )
          
#    autor2 = forms.ModelChoiceField(
#        queryset = OpacAutor.objects.all(),
#        widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete'),
#        required = False
#        )
 
#    autor3 = forms.ModelChoiceField(
#            queryset = OpacAutor.objects.all(),
#            widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete'),
#            required = False
#            )
  
#    autor4 = forms.ModelChoiceField(
#            queryset = OpacAutor.objects.all(),
#            widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete'),
#            required = False
#            )
 


    descriptores = forms.ModelMultipleChoiceField(
        queryset = OpacDescriptor.objects.all(),
        widget = autocomplete.ModelSelect2Multiple(url='opac-descriptor-autocomplete')
        )
    

class OpacInstitucionForm(forms.ModelForm):
    nombre_institucion = forms.ModelChoiceField(
            queryset = OpacInstitucion.objects.all(),
            widget = autocomplete.ModelSelect2(url='opac-institucion-autocomplete')
    )
    


class OpacDocsDigForm(forms.ModelForm):

    autor = forms.ModelChoiceField(
        queryset = OpacAutor.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete')
        )
          
    autor2 = forms.ModelChoiceField(
        queryset = OpacAutor.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete'),
        required = False
        )
    
    autor3 = forms.ModelChoiceField(
        queryset = OpacAutor.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-autor-autocomplete'),
        required = False
        )
    


    descriptor = forms.ModelChoiceField(
        queryset = OpacDescriptor.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-descriptor-autocomplete')
        )


    
    editorial = forms.ModelChoiceField(
        queryset = OpacEditorial.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-editorial-autocomplete')
        )
    

class TesisForm(forms.ModelForm):

       
    
    descriptores = forms.ModelMultipleChoiceField(
        queryset = OpacDescriptor.objects.all(),
        widget = autocomplete.ModelSelect2Multiple(url='opac-descriptor-autocomplete')
        )

    
    autor = forms.ModelChoiceField(
        queryset = OpacTesisAutor.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-tesis-autor-autocomplete')
        )

    autor2 = forms.ModelChoiceField(
        queryset = OpacTesisAutor.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-tesis-autor-autocomplete'),
        required = False
        )
        


    institución = forms.ModelChoiceField(
        queryset = OpacInstitucion.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-institucion-autocomplete')
        )
  
   # cátedra = forms.ModelChoiceField(
   #     queryset = OpacCatedra.objects.all(),
   #     widget = autocomplete.ModelSelect2(url='opac-catedra-autocomplete'),
   #     required=False
   #     )
  
