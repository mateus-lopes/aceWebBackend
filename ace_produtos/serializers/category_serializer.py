from rest_framework.serializers import ModelSerializer
from ace_produtos.models.category import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
