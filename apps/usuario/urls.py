from django.urls import path
from apps.usuario.views import UsuarioCreateView, UsuarioDeleteView, UsuarioListView, UsuarioUpdateView

app_name = "usuario"

urlpatterns = [
    path('', UsuarioListView.as_view(), name='usuario_list'),
    path('nuevo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
]