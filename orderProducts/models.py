from decimal import Decimal

from django.db import models

# Create your models here.
from accounts.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal(0.0))