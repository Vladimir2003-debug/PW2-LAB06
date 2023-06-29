from django.db import models

# Create your models here.

class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField()
    precioTour = models.IntegerField()
    ofertaTour = models.BooleanField()
