from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=11,unique=True)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre