from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ace_produtos.models.product import Product

from uploader.models import Image
from uploader.serializers import ImageSerializer

class ProductSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1

class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", "image"]
        # fields = "__all__"
        # depth = 1