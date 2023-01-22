# DRF imports
from rest_framework import viewsets
from rest_framework.response import Response

# Model import
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

# Extra imports
from drf_spectacular.utils import extend_schema


# class CategoryView(viewsets.ModelViewSet):
#     """
#     A simple viewset for viewing all categories
#     """
#
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
