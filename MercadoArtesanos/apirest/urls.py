from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('producto_create/', Producto_create.as_view(), name="Producto_create"),
    path('producto_update/', Producto_update, name="Producto_update"),
    path('producto_read/<id>/', Producto_read, name="Producto_read"),
    path('producto_read/', Producto_read_all, name='Producto_read_all'),
    path('producto_delete/<id>/', Producto_delete, name="Producto_delete"),
    path('login/', login, name='login'),
]