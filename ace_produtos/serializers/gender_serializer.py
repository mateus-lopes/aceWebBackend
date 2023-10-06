from rest_framework.serializers import ModelSerializer
from ace_produtos.models.gender import Gender

class GenderSerializer(ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"
