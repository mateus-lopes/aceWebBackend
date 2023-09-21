from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ace_produtos.views import CategoriaViewSet, MarcaViewSet, ProdutoViewSet, AutorViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"autores", AutorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]