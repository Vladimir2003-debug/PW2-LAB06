from django.db import models

# Create your models here.

class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    descripcionCiudad = models.CharField(max_length=100)
    imagenCiudad = models.ImageField()
    precioTour = models.CharField(max_length=100)
    ofertaTour = models.BooleanField(default=False)
