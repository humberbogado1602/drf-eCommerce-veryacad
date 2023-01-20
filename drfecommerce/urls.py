from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.product.views import CategoryView

router = routers.DefaultRouter()
router.register(r"category", CategoryView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
