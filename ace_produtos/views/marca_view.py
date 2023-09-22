from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ace_produtos.models.marca import Marca
from ace_produtos.serializers.marca_serializer import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer