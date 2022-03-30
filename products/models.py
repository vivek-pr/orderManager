from decimal import Decimal

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, default="")
    price = models.DecimalField(decimal_places=2, max_digits=8, default=Decimal(0.0))
    quantity = models.IntegerField(default=0)

    def decrease_quantity(self, order_quantity):
        if self.quantity > order_quantity:
            self.quantity -= order_quantity
            self.save()
        else:
            raise ValueError