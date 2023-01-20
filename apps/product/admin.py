from django.contrib import admin

from apps.product.models import Brand, Category, Product

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
