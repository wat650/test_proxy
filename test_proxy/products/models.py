from decimal import Decimal

from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_discounted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def discounted_price(self):
        discount_percentage = Decimal(10)
        return self.price * (Decimal(1) - discount_percentage / Decimal(100))
