from django.db.models.signals import pre_save
from django.dispatch import receiver

from orderProducts.models import Order
from orderProducts.utils import ProductAvailability


@receiver(pre_save, sender=Order)
def order_pre_save(sender, instance, *args, **kwargs):
    try:
        instance.product.decrease_quantity(instance.quantity)
    except ValueError:
        raise ProductAvailability("The product is unavailable in the desired amount.")
