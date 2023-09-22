from django.db import models
from uploader.models import Image
from ace_produtos.models import Autor, Categoria, Marca

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="produtos"
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="produtos"
    )
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    autores = models.ManyToManyField(Autor, related_name="produtos")


    def __str__(self):
        return self.nome