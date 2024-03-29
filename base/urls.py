"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView as login
from base.views import logout_user
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from base.views import error_404, principal
from django.contrib.auth import views as auth_views


handler404 = error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', principal, name='principal'),
    path('usuarios/', include('usuarios.urls')),
   
    path('centroCostos/', include('centroCostos.urls')),
    path('componente/', include('componente.urls')),
    path('recetas/', include('receta.urls')),
    path('ingrediente/', include('ingrediente.urls')),
    path('listaPrecio/', include('listaPrecio.urls')),
    path('ayuda/', include('ayuda.urls')),
    
    path('logout/',logout_user,name="logout"),
    path('',auth_views.LoginView.as_view(),name='inicio'),
    path('', include('django.contrib.auth.urls')),
    path("select2/", include("django_select2.urls")),
    
    

    
    
    
    
 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

