from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ace_produtos.models.category import Category
from ace_produtos.serializers.category_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
