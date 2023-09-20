from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ace_produtos.views import CategoriaViewSet, MarcaViewSet, ProdutoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"produtos", ProdutoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]