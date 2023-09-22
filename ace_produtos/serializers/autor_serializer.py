from rest_framework.serializers import ModelSerializer
from ace_produtos.models.autor import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"