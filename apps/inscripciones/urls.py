from django.urls import path

from apps.inscripciones.views import InscripcionCreateView, InscripcionDeleteView, InscripcionListView, InscripcionUpdateView

app_name = "inscripciones"

urlpatterns = [
    path('', InscripcionListView.as_view(), name='inscripciones_list'),
    path('nuevo/', InscripcionCreateView.as_view(), name='inscripciones_create'),
    path('<int:pk>/editar/', InscripcionUpdateView.as_view(), name='inscripciones_update'),
    path('<int:pk>/eliminar/', InscripcionDeleteView.as_view(), name='inscripciones_delete'),
]