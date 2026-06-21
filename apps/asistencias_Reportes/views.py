
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.asistencias_Reportes.models import Listado


class ListadoListView(ListView):
    model = Listado
    template_name = 'listado/list.html'
    context_object_name = 'listado' 

class ListadoCreateView(CreateView):
    model = Listado
    fields = '__all__'
    template_name = 'listado/create.html'
    success_url = reverse_lazy('listado:listado_list')


class ListadoUpdateView(UpdateView):
    model = Listado
    fields = '__all__'
    template_name = 'listado/update.html'
    success_url = reverse_lazy('listado:listado_list')


class ListadoDeleteView(DeleteView):
    model = Listado
    template_name = 'listado/delete.html'
    success_url = reverse_lazy('listado:listado_list')