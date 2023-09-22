from rest_framework.serializers import ModelSerializer
from ace_produtos.models.marca import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"