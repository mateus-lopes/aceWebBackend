from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ace_produtos.models.product import Product
from ace_produtos.serializers.product_serializer import (
    ProductListSerializer,
    ProductSerializer,
    ProductDetailSerializer
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return ProductListSerializer
    #     elif self.action == "retrieve":
    #         return ProductDetailSerializer
    #     return ProductSerializer

    @action(detail=True, methods=['get'])
    def get_colors(self, request, pk=None):
        product = self.get_object()
        colors = product.get_colors()
        return Response({'colors': colors}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def set_colors(self, request, pk=None):
        product = self.get_object()
        colors = request.data.get('colors', [])
        product.set_colors(colors)
        product.save()
        return Response({'message': 'Cores definidas com sucesso'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_images(self, request, pk=None):
        product = self.get_object()
        images = product.get_images()
        return Response({'images': images}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def set_images(self, request, pk=None):
        product = self.get_object()
        images = request.data.get('images', [])
        product.set_images(images)
        product.save()
        return Response({'message': 'Imagens definidas com sucesso'}, status=status.HTTP_200_OK)
