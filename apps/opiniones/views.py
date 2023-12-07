from typing import Any
from django.db import models
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView

from .forms import OpinionForm
from .models import Opinion

# Create your views here.

def AgregarOpinion(request):
    form = OpinionForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    contexto = {
        'form': form,
    }

    template_name = 'opiniones/agregar_opinion.html'
    return render(request, template_name,contexto)

class ModificarOpinion(LoginRequiredMixin, UpdateView):
    model = Opinion
    fields = ['texto']
    template_name = 'opiniones/modificar_opinion.html'

    def get_success_url(self):
        detalle_url = reverse('apps.discos:detalle_disco', kwargs={'id': self.object.disco.id})
        return detalle_url
    
    def get_context_data(self):
        context = super().get_context_data()
        disco = self.object.disco
        opiniones = Opinion.objects.filter(disco=disco.id)
        context['disco'] = disco
        context['opiniones'] = opiniones
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)
    
class EliminarOpinion(LoginRequiredMixin,DeleteView):
    model = Opinion
    template_name = 'opiniones/confirma_eliminar.html'
    context_object_name = 'opinion'

    def get_success_url(self):
        detalle_url = reverse('apps.discos:detalle_disco', kwargs={'id': self.object.disco.id})
        return detalle_url

