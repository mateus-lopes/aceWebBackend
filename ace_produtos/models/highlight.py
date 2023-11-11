from django.db import models
from uploader.models import Image

class Highlight(models.Model):
    title = models.CharField(max_length=100)
    type_img = models.CharField(max_length=100, choices=(
        ('big', 'Destaque Principal - Slider'),
        ('small', 'Destaque Médio/Pequeno - Pagina Inicial e Menu'),
    ));
    type_product = models.CharField(max_length=100, choices=(
        ('sneaker', 'Tênis'),
        ('accessories', 'Acessórios'),
    ));
    image = models.ForeignKey(
        Image,
        related_name="product",
        on_delete=models.CASCADE,
        blank=True,
    )
    url = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
