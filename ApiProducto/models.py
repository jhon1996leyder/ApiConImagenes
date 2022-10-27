from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre_produc = models.CharField(max_length=60)
    precio_produc = models.PositiveIntegerField(default=0)
    descripcion_produc = models.CharField(max_length=60)
    imagen_produc = models.ImageField(upload_to="productos", null = True)
    
