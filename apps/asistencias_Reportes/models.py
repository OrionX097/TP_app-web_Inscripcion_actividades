from django.db import models

from apps.inscripciones.models import Inscripcion

# Create your models here.
class Listado(models.Model):
    id_inscripcion = models.ForeignKey(Inscripcion,on_delete=models.CASCADE)
    fecha_clase = models.CharField(max_length=20)
    asistencia = models.CharField(max_length=20)

    def __str__(self):
        return self.fecha_clase