from django.http import request
from django.shortcuts import render , redirect
from .models import Producto , PerfilUsuario
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required , permission_required



def AboutUs(request):
    return render(request , "ArtesanosApp/aboutUs.html")

def Contacto_artesanos(request):
    return render(request , "ArtesanosApp/contacto_artesanos.html")


def Home(request):
    data = {"lista":Producto.objects.all().order_by('id')[0:4] , "lista2":Producto.objects.all().order_by('precio')[5:9]}
    return render(request , "ArtesanosApp/home.html" , data)

def Producto_principal(request , id):
    producto = Producto.objects.get(id=id)
    data = {"lista": producto}
    return render(request , "ArtesanosApp/producto_principal.html", data)

def Productos(request):
    data = {"lista":Producto.objects.all().order_by('id')}
    return render(request , "ArtesanosApp/productos.html", data)

def Registro_artesanos(request):
    return render(request , "ArtesanosApp/registro_artesanos.html")


def Productos_conf(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    messages.success(request,"¡El Producto fue creado correctamente!")
                    return redirect(to="listar_productos")
                except:
                    messages.warning(request,"No pueden existir productos con el mismo ID")

    elif action == 'upd':
        objeto = Producto.objects.get(id=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid():
                form.save()
                messages.success(request, "¡El producto fue actualizado correctamente!")
                return redirect(to="listar_productos")
        data["form"] = ProductoForm(instance=objeto)

    elif action == 'del':
        try:
            Producto.objects.get(id=id).delete()
            return redirect(to="listar_productos")
        except:
            messages.error(request,"¡El Producto ya estaba eliminado!")
    data["list"] = Producto.objects.all().order_by('id')
    return render(request, "ArtesanosApp/conf_producto.html", data)

def Listar_productos(request):
    data = {"list":Producto.objects.all().order_by('id')}
    return render(request, 'ArtesanosApp/lista_productos.html', data)

def registro(request):
    data = {'form': CustomUserCreationForms}
    if request.method == 'POST':
        formulario = CustomUserCreationForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Te has registrado correctamente")
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
    return render(request , 'registration/registro.html', data)


def perfil_usuario(request):
    data = {"mesg": "", "form": PerfilUsuarioForm}

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.save()
            perfil = PerfilUsuario.objects.get(user=user)
            perfil.rut = request.POST.get("rut")
            perfil.direccion = request.POST.get("direccion")
            perfil.save()
            data["mesg"] = "¡Sus datos fueron actualizados correctamente!"

    perfil = PerfilUsuario.objects.get(user=request.user)
    form = PerfilUsuarioForm()
    form.fields['first_name'].initial = request.user.first_name
    form.fields['last_name'].initial = request.user.last_name
    form.fields['email'].initial = request.user.email
    form.fields['rut'].initial = perfil.rut
    form.fields['direccion'].initial = perfil.direccion
    data["form"] = form
    return render(request, "ArtesanosApp/perfil_usuario.html", data)

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                rut = request.POST.get("rut")
                direccion = request.POST.get("direccion")
                PerfilUsuario.objects.update_or_create(user=user, rut=rut, direccion=direccion)
                messages.success(request, "Se ha creado el usuario exitosamente")
                # DEJAMOS AL USUARIO AUTHENTICADO Y LOGEADO DE MANERA AUTOMÁTICA
                auth = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
                login(request, auth)
                return redirect(to="home")
            except:
                redirect(to="registrar_usuario")
    form = RegistrarUsuarioForm()
    
    return render(request, "ArtesanosApp/registrar_usuario.html", context={'form': form})

def iniciar_sesion(request):
    data = {"mesg": "", "form": IniciarSesionForm()}

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to="home")
                else:
                    data["mesg"] = "¡La cuenta o la password no son correctos!"
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, "ArtesanosApp/iniciar_sesion.html", data)

def cerrar_sesion(request):
    logout(request)
    return redirect(to="home")
