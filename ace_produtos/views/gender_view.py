from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ace_produtos.models.gender import Gender
from ace_produtos.serializers.gender_serializer import GenderSerializer

class GenderViewSet(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
