from django.shortcuts import render
from .models import DiscountedProduct


def discounted_products_view(request):
    discounted_products = DiscountedProduct.objects.filter(is_discounted=True)
    print(discounted_products)
    return render(request, 'products/discounted_products.html', {
        'discounted_products': discounted_products
    })
