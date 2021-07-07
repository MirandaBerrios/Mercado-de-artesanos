from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from ArtesanosApp.models import Producto
from .serializers import ProductoSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import viewsets 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Producto_create(APIView):
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Producto_update(APIView):
    def put(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Producto_read(request, id):
    if request.method == 'GET':
        objeto = get_object_or_404(Producto, id=id)
        serializer = ProductoSerializer(objeto)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def Producto_read_all(request):
    if request.method == 'GET':
        list = Producto.objects.all()
        serializer = ProductoSerializer(list, many=True)
        return Response(serializer.data)
    

@api_view(['DELETE'])
def Producto_delete(request, id):
    if request.method == 'DELETE':
        try:
            Producto.objects.get(id=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    password_valida = check_password(password, user.password)
    if not password_valida:
        return Response("Contraseña incorrecta")
    token, created = Token.objects.get_or_create(user=user)
    print(f"Este es el token creado: '{token.key}'")
    return Response(token.key)