from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase
from orderProducts.models import Order, User, Product
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class ProductTestCase(APITestCase):

    def setUp(self):
        self.url = '/products/'
        self.product = Product.objects.create(name="watch", price=Decimal(12.2), quantity=12)
        self.user = User.objects.create(username="testuser", email="testuser@yopmail.com", password="Insure12")

    def get_client(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        return client

    def get_token_client(self):
        client = APIClient()
        token = Token.objects.get(user=self.user)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
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

    def test_post_not_allowed(self):
        resp = self.get_client().post(self.url, {}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_token_get(self):
        resp = self.get_token_client().get(self.url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)