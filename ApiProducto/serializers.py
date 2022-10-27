from rest_framework import serializers
from .models import Producto

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre_produc', 'precio_produc', 'descripcion_produc', 'imagen_produc')