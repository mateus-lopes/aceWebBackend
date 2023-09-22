from django.contrib import admin

from .models import Categoria, Marca, Produto, Autor


admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(Autor)