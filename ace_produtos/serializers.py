from rest_framework.serializers import ModelSerializer
from ace_produtos.models import Categoria, Marca, Produto, Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "preco"]