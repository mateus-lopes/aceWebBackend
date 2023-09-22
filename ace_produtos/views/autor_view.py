from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ace_produtos.models.autor import Autor
from ace_produtos.serializers.autor_serializer import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer