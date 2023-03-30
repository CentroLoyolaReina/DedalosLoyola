from django import forms
from .models import RegistroUsuarios, OpacLibro, OpacUsuario, OpacDescriptor, OpacInstitucion
from dal import autocomplete


    

class OpacLibroUsuarioForm(forms.ModelForm):

#    descriptor = forms.ModelChoiceField(
#        queryset = OpacDescriptor.objects.all(),
#        widget = autocomplete.ModelSelect2(url='opac-descriptor-autocomplete')
#        )

    recurso_prestamo = forms.ModelChoiceField(
        queryset = OpacLibro.objects.all(),
        widget = autocomplete.ModelSelect2(url='opac-libro-autocomplete')
        )
    #    
    #nombre_apellidos = forms.ModelChoiceField(
    #        queryset = OpacUsuario.objects.all(),
    #        widget = autocomplete.ModelSelect2(url='reg-usuarios-autocomplete')
    #        )



    institucion  = forms.ModelChoiceField(
            queryset = OpacInstitucion.objects.all(),
            widget = autocomplete.ModelSelect2(url='opac-institucion-autocomplete')
            )

