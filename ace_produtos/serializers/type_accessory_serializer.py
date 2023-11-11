from rest_framework.serializers import ModelSerializer
from ace_produtos.models.type_accessory import TypeAccessory

class TypeAccessorySerializer(ModelSerializer):
    class Meta:
        model = TypeAccessory
        fields = "__all__"
        depth = 1
