from django.shortcuts import render, redirect
from django.views.defaults import page_not_found


def inicio(request):
    context={}
    return render(request,'ingreso.html',context)

def principal(request):
    titulo="Menu Principal"
    context={
        'titulo':titulo
    }
    return render(request,'menu.html',context)

def error_404(request,exception):
    context={}
    return render(request,'404.html',context)

