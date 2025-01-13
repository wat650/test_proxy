from django.urls import path
from .views import discounted_products_view

app_name = "products"

urlpatterns = [
    path("discounted_products/", discounted_products_view, name="discounted_products"),
]
