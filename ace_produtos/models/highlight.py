from django.db import models
from uploader.models import Image

class Highlight(models.Model):
    title = models.CharField(max_length=100)
    image = models.ForeignKey(
        Image,
        related_name="product",
        on_delete=models.CASCADE,
        blank=True,
    )
    url = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
