from django.urls import path
from apps.actividades.views import ActividadCreateView, ActividadDeleteView, ActividadListView, ActividadUpdateView

app_name = "actividades"

urlpatterns = [
    path('', ActividadListView.as_view(), name='list'),
    path('nuevo/', ActividadCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', ActividadUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', ActividadDeleteView.as_view(), name='delete'),
]