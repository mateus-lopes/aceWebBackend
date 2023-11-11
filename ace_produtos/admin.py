from django.contrib import admin

from .models import Category, Product, Gender, Highlight, TypeAccessory

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

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_img', 'type_product')
    search_fields = ('title', 'type_img', 'type_product')
    list_filter = ('title', 'type_img', 'type_product')
    ordering = ('title', 'type_img', 'type_product')

@admin.register(TypeAccessory)
class TypeAccessoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)




