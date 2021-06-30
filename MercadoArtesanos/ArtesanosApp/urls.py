from django.urls import path
from .views import *

urlpatterns = [
     path('', Home , name="home"),
     path('aboutUs', AboutUs, name="aboutUs"),
     path('contacto_artesano', Contacto_artesanos, name="contacto_artesanos"),
     path('productos', Productos, name="productos"),
     path('registro_artesanos', Registro_artesanos, name="registro_artesanos"),
     path('producto_principal', Producto_principal, name="producto-principal"),
     path('conf/<action>/<id>', Productos_conf, name="conf_producto"),
     path('conf', Listar_productos, name="listar_productos")

]
