from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
        id = models.IntegerField(primary_key=True, verbose_name="Id producto") 
        nombre_producto = models.CharField(max_length=30 , blank=False , null=False , verbose_name="nombre del producto")
        precio = models.IntegerField(blank=False , null=False ,verbose_name="precio del producto")
        descripcion = models.CharField(max_length=1000 , blank=False , null=False , verbose_name = "descripcion del producto" )
        image = models.ImageField(upload_to ='images/' , default='nostock.jpg', blank=False , null=False  , verbose_name = "imagen del producto")
        def __str__(self):
            return self.nombre_producto



class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")
 
    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name} ({self.user.email})"








