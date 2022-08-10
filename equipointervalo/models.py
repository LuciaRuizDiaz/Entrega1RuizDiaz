from django.db import models

# Create your models here.
class Profesionales (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    
class Areas (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)

class Servicios (models.Model):
    nombre = models.CharField(max_length=50)
    areaejecutora = models.CharField(max_length=50)
    
    
    