from rest_framework import serializers , fields
from ArtesanosApp.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'