from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy,reverse

from .models import Categoria, Discos
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm

# Create your views here.

class AgregarCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'discos/agregar_categoria.html'
    success_url = reverse_lazy('inicio')

class AgregarDisco(CreateView):
    model = Discos
    fields = ['titulo', 'autor', 'letra', 'imagen', 'categoria']
    template_name = 'discos/agregar_disco.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self,form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)
    
class ModificarDisco(UpdateView):
    model = Discos
    fields = ['titulo', 'autor', 'letra', 'imagen', 'categoria']
    template_name = 'discos/agregar_disco.html'
    success_url = reverse_lazy('inicio')

class ListarDiscos(ListView):
    model = Discos
    template_name = 'discos/listar_discos.html'
    context_object_name = 'discos'
    paginate_by = 3

    def get_context_data(self) :
        context = super().get_context_data()
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains = query)
        return queryset.order_by('titulo')

class EliminarDisco(DeleteView):
    model = Discos
    template_name = 'discos/confirma_eliminar.html'
    success_url = reverse_lazy('inicio')

# class DiscoDetalle(DetailView):
#     model = Discos
#     template_name = 'discos/disco_detalle.html'
#     context_object_name = 'disco'

def disco_detalle(request,id):
    disco = Discos.objects.get(id=id)
    opiniones = Opinion.objects.filter(disco=id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.disco = disco
            aux.usuario = request.user
            aux.save()
            detalle_url = reverse('apps.discos:detalle_disco', kwargs={'id': disco.id})
            return HttpResponseRedirect(detalle_url)
        else:
            return redirect('apps.usuarios:iniciar_sesion')
    
    contexto = {
        'disco': disco,
        'form': form,
        'opiniones': opiniones
    }
    template_name = 'discos/disco_detalle.html'
    return render(request,template_name,contexto)

def listar_por_categoria(request, categoria):
    categoria = Categoria.objects.filter(nombre = categoria)
    discos = Discos.objects.filter(categoria = categoria[0].id).order_by('fecha_agregado')
    categorias = Categoria.objects.all()
    template_name = 'discos/listar_discos.html'
    contexto = {
        'discos' : discos,
        'categorias' : categorias        
    }
    return render(request,template_name,contexto)

# -----------Ejemplo de : Ordenar por  ----------------------

def ordenar_por(request):
    # Obtenemos el dato de 'orden' de la URL -> metodo GET ( para esto tiene que haber un elemento html que contenga el name = 'orden' y el valor(value=''))
    orden = request.GET.get('orden', '')
    #Validar lo que contiene Value
    if orden == 'fecha':
        discos = Discos.objects.order_by('fecha_agregado')
    elif orden == 'titulo':
        discos = Discos.objects.order_by('titulo')
    else:
        discos = Discos.objects.all()
    template_name = 'discos/listar_discos.html'
    contexto = {
        'discos' : discos
    }
    return render(request, template_name, contexto)