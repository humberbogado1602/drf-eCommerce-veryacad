from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.product.views import CategoryViewSet, BrandViewSet, ProductViewSet

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"brand", BrandViewSet)
router.register(r"product", ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
