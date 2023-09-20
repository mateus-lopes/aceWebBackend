from django.contrib import admin
from .models import Categoria, Marca, Produto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Produto)