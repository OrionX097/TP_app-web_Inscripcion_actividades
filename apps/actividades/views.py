
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.actividades.models import Actividad



class ActividadListView(ListView):
    model = Actividad
    template_name = 'actividades/list.html'
    context_object_name = 'actividades' 

class ActividadCreateView(CreateView):
    model = Actividad
    fields = '__all__'
    template_name = 'actividades/create.html'
    success_url = reverse_lazy('actividades:list')


class ActividadUpdateView(UpdateView):
    model = Actividad
    fields = '__all__'
    template_name = 'actividades/update.html'
    success_url = reverse_lazy('actividades:list')


class ActividadDeleteView(DeleteView):
    model = Actividad
    template_name = 'actividades/delete.html'
    success_url = reverse_lazy('actividades:list')