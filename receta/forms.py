from django.forms import ModelForm, widgets
from django_select2 import forms as s2forms
from receta.models import Receta
from django import forms
from .models import Receta, Ingrediente


from django import forms

class MyForm(forms.Form):
    phone = forms.BooleanField(required=True)

class IngredienteWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains",
        "id__icontains"
    }
        
class recetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nomComponente', 'codReceta', 'nomReceta', 'estado', 'estandar', 'preparacion','ingredientes']
        widgets = {
            'ingredientes': forms.CheckboxSelectMultiple(),
        }