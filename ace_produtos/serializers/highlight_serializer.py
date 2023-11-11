from rest_framework.serializers import ModelSerializer
from ace_produtos.models.highlight import Highlight

class HighlightSerializer(ModelSerializer):
    class Meta:
        model = Highlight
        fields = "__all__"
        depth = 1