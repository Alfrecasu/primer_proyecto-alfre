from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {'valor': 50 }
    return render(request, template_name, context)

def contacto(request):
    template_name = 'contacto.html'
    nombres = ['Informatorio', 'Ceci', 'Vane']
    context = {'nombres': nombres }
    return render(request, template_name, context)