from django.http import request
from django.shortcuts import render , redirect
from .models import Producto
from .forms import ProductoForm , CustomUserCreationForms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required , permission_required



def AboutUs(request):
    return render(request , "ArtesanosApp/aboutUs.html")

def Contacto_artesanos(request):
    return render(request , "ArtesanosApp/contacto_artesanos.html")


def Home(request):
    data = {"lista":Producto.objects.all().order_by('id')[0:4] , "lista2":Producto.objects.all().order_by('precio')[8:12]}
    return render(request , "ArtesanosApp/home.html" , data)

def Producto_principal(request):
    return render(request , "ArtesanosApp/producto_principal.html")

def Productos(request):
    data = {"lista":Producto.objects.all().order_by('id')}
    return render(request , "ArtesanosApp/productos.html", data)

def Registro_artesanos(request):
    return render(request , "ArtesanosApp/registro_artesanos.html")

# def poblar_bd(request):
#     Producto.objects.create(ID=1 , NOMBRE_PRODUCTO='Chaslina', PRECIO= 9890 ,  DESCRIPCION="Fabricada con lana pigmentada \
#                             con tintes naturales", IMAGE='../static/image/chaslina.jpg').objetcts.get

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