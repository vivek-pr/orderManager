from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase
from orderProducts.models import Order, User, Product
from rest_framework.test import APIClient


class OrderTestCase(APITestCase):

    def setUp(self):
        self.url = '/orders/'
        self.product = Product.objects.create(name="watch", price=Decimal(12.2), quantity=12)
        self.user = User.objects.create(username="testuser", email="testuser@yopmail.com", password="Insure12")
        self.payload = {'user': self.user.id, 'product': self.product.id, 'quantity': 1, 'amount_paid': Decimal(12.2)}

    def get_client(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        return client

    def test_list_order_forbidden(self):
        """
        Ensure Get request return value
        :return:
        """

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_json(self):
        resp = self.get_client().get(self.url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_order_forbidden(self):
        """
        Ensure Get request return value
        :return:
        """

        response = self.client.post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_order(self):
        """
        Ensure we can create a new account object.
        """

        response = self.get_client().post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().quantity, 1)
        self.assertEqual(Order.objects.get().product.quantity, 11)

    def test_create_order_quantity_fail(self):
        payload = self.payload
        payload['quantity'] = 14
        response = self.get_client().post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_create_order_activity_count(self):
        """
        Ensure we can create a new account object.
        """

        response = self.get_client().post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        resp = self.get_client().get(self.url, format='json')
        self.assertEqual(len(resp.data['results']), 1)

