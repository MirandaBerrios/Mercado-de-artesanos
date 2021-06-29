from django.db import models


class Producto(models.Model):
        id = models.IntegerField(primary_key=True, verbose_name="Id producto") 
        nombre_producto = models.CharField(max_length=30 , blank=False , null=False , verbose_name="nombre del producto")
        precio = models.IntegerField(blank=False , null=False ,verbose_name="precio del producto")
        descripcion = models.CharField(max_length=1000 , blank=False , null=False , verbose_name = "descripcion del producto" )
        image = models.ImageField(upload_to ='images/' , default = "no_stock.jpg", blank=False , null=False  , verbose_name = "imagen del producto")
        def __str__(self):
            return self.nombre_producto












