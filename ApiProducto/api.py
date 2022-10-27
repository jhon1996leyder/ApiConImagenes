from .models import Producto
from rest_framework import viewsets, permissions
from .serializers import ProductosSerializer

class ProductoviewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosSerializer