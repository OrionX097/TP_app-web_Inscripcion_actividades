from django.urls import path

from apps.asistencias_Reportes.views import ListadoCreateView, ListadoDeleteView, ListadoListView, ListadoUpdateView

app_name = "asistencias_Reportes"

urlpatterns = [
    path('', ListadoListView.as_view(), name='list'),
    path('nuevo/', ListadoCreateView.as_view(), name='asistencias_Reportes_create'),
    path('<int:pk>/editar/', ListadoUpdateView.as_view(), name='asistencias_Reportes_update'),
    path('<int:pk>/eliminar/', ListadoDeleteView.as_view(), name='asistencias_Reportes_delete'),
]