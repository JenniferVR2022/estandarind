from django import forms
from django.forms import ModelChoiceField, ModelForm
from django_select2 import forms as s2forms
from receta.models import Receta, Ingrediente

class IngredienteWidget(s2forms.ModelSelect2Widget):
    search_fields = {
        "nombre__icontains",
        "id__icontains"
    }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nomComponente', 'codReceta', 'nomReceta', 'estado', 'estandar', 'preparacion', 'observacion', 'ingredientes']
        widgets = {
            'ingredientes': IngredienteWidget(),
        }
