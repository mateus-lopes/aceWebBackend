from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from ace_produtos.models.product import Product 
from ace_produtos.serializers.product_serializer import ProductListSerializer, ProductSerializer, ProductDetailSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer
        return ProductSerializer

    @action(detail=True, methods=['get'])
    def get_cores(self, request, pk=None):
        product = self.get_object()
        cores = product.get_cores()
        return Response({'cores': cores}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def set_cores(self, request, pk=None):
        product = self.get_object()
        cores = request.data.get('cores', [])
        product.set_cores(cores)
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