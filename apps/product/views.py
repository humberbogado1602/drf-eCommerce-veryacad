# DRF imports
from rest_framework import viewsets
from rest_framework.response import Response

# Model import
from .models import Category
from .serializers import CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    """
    A simple viewset for viewing all categories
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class CategoryView(viewsets.ViewSet):
#     """
#     A simple viewset for viewing all categories
#     """
#
#     queryset = Category.objects.all()
#
#     def list(self, request):
#         serializer = CategorySerializer(self.queryset, many=True)
#         return Response(serializer.data)
#
