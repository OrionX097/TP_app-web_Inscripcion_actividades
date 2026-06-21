from django.db import models

# Create your models here.
class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    dias = models.CharField(max_length=40)
    horario = models.CharField(max_length=20)
    cupo_max = models.IntegerField()
    cupo_disponible = models.IntegerField()

    def __str__(self):
        return self.nombre