from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ace_produtos.models.produto import Produto

from uploader.models import Image
from uploader.serializers import ImageSerializer

class ProdutoSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        # fields = ["id", "nome", "preco", "imagem"]
        fields = "__all__"
        depth = 1