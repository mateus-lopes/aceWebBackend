from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from ace_produtos.models.produto import Produto 
from ace_produtos.serializers.produto_serializer import ProdutoListSerializer, ProdutoSerializer, ProdutoDetailSerializer

class ProdutoViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    queryset = Produto.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer

    @action(detail=True, methods=['get'])
    def get_cores(self, request, pk=None):
        produto = self.get_object()
        cores = produto.get_cores()
        return Response({'cores': cores}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def set_cores(self, request, pk=None):
        produto = self.get_object()
        cores = request.data.get('cores', [])
        produto.set_cores(cores)
        produto.save()
        return Response({'message': 'Cores definidas com sucesso'}, status=status.HTTP_200_OK)
