
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.actividades.models import Actividad



class ActividadListView(ListView):
    model = Actividad
    template_name = 'actividad/list.html'
    context_object_name = 'actividad' 

class ActividadCreateView(CreateView):
    model = Actividad
    fields = '__all__'
    template_name = 'actividad/create.html'
    success_url = reverse_lazy('actividad:actividad_list')


class ActividadUpdateView(UpdateView):
    model = Actividad
    fields = '__all__'
    template_name = 'actividad/update.html'
    success_url = reverse_lazy('actividad:actividad_list')


class ActividadDeleteView(DeleteView):
    model = Actividad
    template_name = 'actividad/delete.html'
    success_url = reverse_lazy('actividad:actividad_list')