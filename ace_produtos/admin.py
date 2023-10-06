from django.contrib import admin

from .models import Category, Product, Gender

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    search_fields = ('title', 'category__descricao')
    list_filter = ('category', 'price', 'promotion')
    ordering = ('title', 'category')
    list_per_page = 25