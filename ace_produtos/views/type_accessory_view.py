from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ace_produtos.models.type_accessory import TypeAccessory
from ace_produtos.serializers.type_accessory_serializer import TypeAccessorySerializer

class TypeAccessoryViewSet(ModelViewSet):
    queryset = TypeAccessory.objects.all()
    serializer_class = TypeAccessorySerializer
