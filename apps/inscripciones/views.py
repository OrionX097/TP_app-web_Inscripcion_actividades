
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.inscripciones.models import Inscripcion 



class InscripcionListView(ListView):
    model = Inscripcion
    template_name = 'inscripcion/list.html'
    context_object_name = 'inscripcion' 

class InscripcionCreateView(CreateView):
    model = Inscripcion
    fields = '__all__'
    template_name = 'inscripcion/create.html'
    success_url = reverse_lazy('inscripcion:inscripcion_list')


class InscripcionUpdateView(UpdateView):
    model = Inscripcion
    fields = '__all__'
    template_name = 'inscripcion/update.html'
    success_url = reverse_lazy('inscripcion:inscripcion_list')


class InscripcionDeleteView(DeleteView):
    model = Inscripcion
    template_name = 'inscripcion/delete.html'
    success_url = reverse_lazy('inscripcion:inscripcion_list')