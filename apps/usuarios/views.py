from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Usuarios
from .forms import RegitrarUsuariosForm

# Create your views here.
class RegitrarUsuario(CreateView):
    model = Usuarios
    form_class = RegitrarUsuariosForm
    template_name = 'usuarios/registrar_usuarios.html'
    success_url = reverse_lazy('inicio')

class ActualizarUsuario(LoginRequiredMixin,UpdateView):
    model = Usuarios
    fields= ['nombre','apellido','email','fecha_nacimiento', 'imagen']
    template_name = 'usuarios/registrar_usuarios.html'
    success_url = reverse_lazy('inicio')

class EliminarUsuario(LoginRequiredMixin,DeleteView):
    model = Usuarios
    template_name = 'discos/confirma_eliminar.html'
    success_url = reverse_lazy('apps.usuarios:listar_usuarios')

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    template_name = 'usuarios/listar_usuarios.html'
    contexto = {
        "usuarios" : usuarios
    }
    return render(request, template_name, contexto)