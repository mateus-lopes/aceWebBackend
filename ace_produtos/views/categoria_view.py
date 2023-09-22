from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ace_produtos.models.categoria import Categoria
from ace_produtos.serializers.categoria_serializer import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
