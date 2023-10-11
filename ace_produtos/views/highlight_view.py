from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ace_produtos.models.highlight import Highlight
from ace_produtos.serializers.highlight_serializer import HighlightSerializer

class HighlightViewSet(ModelViewSet):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer