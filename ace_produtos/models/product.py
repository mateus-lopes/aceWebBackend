from django.db import models
from uploader.models import Image
from ace_produtos.models import Category, Gender

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    promotion = models.DecimalField(max_digits=8, decimal_places=0)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="produtos"
    )
    gender = models.ForeignKey(
        Gender, on_delete=models.PROTECT, related_name="produtos"
    )
    images = models.ManyToManyField(
        Image,
        related_name="products",
        blank=True,
    )
    colors = models.CharField(max_length=255)  

    def __str__(self):
        return self.title

    def set_colors(self, colors_list):
        self.colors = ",".join(colors_list)

    def get_colors(self):
        return self.colors.split(",")

    def get_images(self):
        return [image.url for image in self.images.all()]