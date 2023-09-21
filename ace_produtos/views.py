from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ace_produtos.models import Categoria, Marca, Produto, Autor
from ace_produtos.serializers import CategoriaSerializer, MarcaSerializer, ProdutoListSerializer, ProdutoSerializer, ProdutoDetailSerializer, AutorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer
    
class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer