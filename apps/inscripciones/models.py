from django.db import models
from apps.actividades.models import Actividad
from apps.usuario.models import Usuario

# Create your models here.
class Inscripcion(models.Model):
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_actividad = models.ForeignKey(Actividad,on_delete=models.CASCADE)
    fecha_inscripcion = models.CharField(max_length=20)
    estado = models.CharField(max_length=30)

    def __str__(self):
        return self.fecha_inscripcion