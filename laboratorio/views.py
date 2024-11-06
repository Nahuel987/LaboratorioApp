from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Listar todos los laboratorios


class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio_list.html'

# Crear un nuevo laboratorio


class LaboratorioCreateView(CreateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'laboratorio_form.html'
    success_url = reverse_lazy('laboratorio_list')

# Actualizar un laboratorio existente


class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'laboratorio_form.html'
    success_url = reverse_lazy('laboratorio_list')

# Eliminar un laboratorio


class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio_confirm_delete.html'
    success_url = reverse_lazy('laboratorio_list')
