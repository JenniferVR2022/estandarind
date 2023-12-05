from django import forms
from django.forms import ModelChoiceField, ModelForm
from django_select2 import forms as s2forms
from receta.models import Receta, Ingrediente, Componente

class IngredienteWidget(s2forms.ModelSelect2Widget):
    search_fields = {
        "nombre__icontains",
        "id__icontains"
    }
    
    

class recetaForm(forms.ModelForm):
    ingredientes = forms.ModelMultipleChoiceField(
        queryset=Ingrediente.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Receta
        fields = ['nomComponente', 'codReceta', 'nomReceta', 'estado', 'estandar', 'preparacion', 'observacion', 'ingredientes']
