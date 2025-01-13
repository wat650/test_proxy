from django.contrib import admin
from .models import Product, DiscountedProduct

# Register your models here.
admin.site.register(Product),
admin.site.register(DiscountedProduct),
