from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ace_produtos.models.produto import Produto 
from ace_produtos.serializers.produto_serializer import ProdutoListSerializer, ProdutoSerializer, ProdutoDetailSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer