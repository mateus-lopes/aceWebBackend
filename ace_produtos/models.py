from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

# class Autor(models.Model):
#     nome = models.CharField(max_length=100)
#     email = models.EmailField(null=True, blank=True)

#     def __str__(self):
#         return self.nome
    
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
    
    # autores = models.ManyToManyField(Autor, related_name="livros")


    def __str__(self):
        return self.nome
    
    # class Meta:
    #         verbose_name = "Produto"
    #         verbose_name_plural = "Produtos-Teste"