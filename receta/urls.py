from django.urls import path
from receta.views import listar_recetas,receta_crear,receta_agregar,editarR,eliminar,detalle_receta,seleccionar_ingredientes
from . import views

urlpatterns = [
    path('', views.listar_recetas, name='listar_recetas'),
    path('crear/', views.receta_crear, name='crear-receta'),
    path('agregar/', views.receta_agregar, name='receta-agregar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('editarR/<int:pk>/', views.editarR, name='editarR'),
    path('detalle-receta/<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('seleccionar-ingredientes/', seleccionar_ingredientes, name='seleccionar_ingredientes'),
]



    










    

