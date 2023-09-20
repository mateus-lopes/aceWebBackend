from django.contrib import admin
from .models import Categoria, Marca, Produto

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Produto)