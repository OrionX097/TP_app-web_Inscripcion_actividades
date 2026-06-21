
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.usuario.models import Usuario




class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario/list.html'
    context_object_name = 'usuario' 

class UsuarioCreateView(CreateView):
    model = Usuario
    fields = '__all__'
    template_name = 'usuario/create.html'
    success_url = reverse_lazy('usuario:usuario_list')


class UsuarioUpdateView(UpdateView):
    model = Usuario
    fields = '__all__'
    template_name = 'usuario/update.html'
    success_url = reverse_lazy('usuario:usuario_list')


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario/delete.html'
    success_url = reverse_lazy('usuario:usuario_list')