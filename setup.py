import random

from accounts.models import User
from orderProducts.models import Order
from products.models import Product

MAX_USER = 10
MAX_PRODUCT = 100
MAX_TRANSACTION = 1000


def setup_users():
    user_name = "test_user"
    pass_word = "Insure12"
    for i in range(MAX_USER):
        User.objects.create_user(f'{user_name}_{i}', email=f'{user_name}_{i}@yopmail.com',
                                 password=pass_word, is_active=True)


def setup_products():
    product_name = "dummy"
    price = 12.25
    quantity = 100
    for i in range(MAX_PRODUCT):
        new_price = price + i
        quantity = quantity + i
        Product.objects.create(name=f"{product_name}_i", price=new_price, quantity=quantity)


def setup_orders():
    """
    NOTE: This setup will work only for db setup from scratch
    :return:
    """
    amount_paid = 12
    quantity = 1

    for i in range(MAX_TRANSACTION):
        user = random.randint(1, MAX_USER)
        product_id = random.randint(1, MAX_PRODUCT)
        Order.objects.create(amount_paid=amount_paid, quantity=quantity,
                             user_id=user, product_id=product_id)


setup_users()
setup_products()
setup_orders()