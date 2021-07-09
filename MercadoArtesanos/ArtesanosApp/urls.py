from django.urls import path
from .views import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', Home , name="home"),
     path('aboutUs', AboutUs, name="aboutUs"),
     path('contacto_artesano', Contacto_artesanos, name="contacto_artesanos"),
     path('productos', Productos, name="productos"),
     path('registro_artesanos', Registro_artesanos, name="registro_artesanos"),
     path('producto_principal/<id>', Producto_principal, name="producto_principal"),
     path('conf/<action>/<id>', Productos_conf, name="conf_producto"),
     path('conf', Listar_productos, name="listar_productos"),
     path('registro/', registrar_usuario, name="registro"),
     path('password_cambiada/', TemplateView.as_view(template_name='core/password_cambiada.html'), name='password_cambiada'),
     path('cambio_contrasena/', auth_views.PasswordChangeView.as_view(template_name='ArtesanosApp/cambiar_contrasena.html', success_url='/password_cambiada'), name='cambiar_password'),
     path('perfil_usuario/', perfil_usuario, name="perfil_usuario"),
     path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
     path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),




]
