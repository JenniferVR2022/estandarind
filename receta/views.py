from django.shortcuts import render, redirect,get_object_or_404
from receta.forms import recetaForm
from ingrediente.models import Ingrediente
from .models import Receta, Ingrediente,Componente
from .forms import recetaForm
from django.contrib.auth.decorators import login_required
from .models import Receta

@login_required
def listar_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'receta/receta.html', {'recetas': recetas})


def receta_crear(request):
    if request.method == 'POST':
        form = recetaForm(request.POST)
        if form.is_valid():
            receta = form.save(commit=False)
            componente_id = request.POST.get('nomComponente')  # Obtén el ID del componente seleccionado
            componente = Componente.objects.get(pk=componente_id)  # Obtén la instancia del componente
            receta.nomComponente = componente  # Asigna la instancia del componente
            receta.save()
            
            # Procesa los ingredientes seleccionados
            ingredientes_seleccionados = request.POST.get('ingredientes_seleccionados')
            lista_ingredientes = ingredientes_seleccionados.split(',') if ingredientes_seleccionados else []
            receta.ingredientes.add(*lista_ingredientes)  # Agrega los ingredientes a la relación muchos-a-muchos
            
            return redirect('detalle_receta', pk=receta.pk)
    else:
        form = recetaForm()
    ingredientes = Ingrediente.objects.all()
    return render(request, 'receta/recetaCrear.html', {'form': form, 'ingredientes': ingredientes})





def seleccionar_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'receta/ingredientes.html', {'ingredientes': ingredientes})


@login_required
def receta_agregar(request):
    Ingredientes = Ingrediente.objects.values_list('nomIngrediente', flat=True)
    context = {
        'ingrediente': Ingredientes,   
    }
    return render(request, 'receta/recetaAgregar.html', context)

def eliminar(request,id):
    receta = Receta.objects.get(id=id)
    receta.estado = False
    receta.save()
    return redirect('receta')


@login_required
def editarR(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        form = recetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            
            # Procesar ingredientes seleccionados
            ingredientes_seleccionados = request.POST.get('ingredientes_seleccionados')
            lista_ingredientes = ingredientes_seleccionados.split(',') if ingredientes_seleccionados else []
            receta.ingredientes.set(lista_ingredientes)  # Establecer la relación de ingredientes
            
            return redirect('detalle_receta', pk=pk)
    else:
        form = recetaForm(instance=receta)
    return render(request, 'receta/editarReceta.html', {'form': form, 'receta': receta})



@login_required
def detalle_receta(request, pk):
    receta = Receta.objects.get(id=pk)
    return render(request, 'receta/detalle_receta.html', {'receta': receta})

