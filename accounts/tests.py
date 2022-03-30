from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from orderProducts.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.url = '/api-token-auth/'
        self.username = 'vivekp'
        self.email = 'vivek@example.com'
        self.password = "Insure12"
        self.user = User.objects.create_superuser(username=self.username,
                                                  email=self.email, password=self.password, is_active=True)

    def test_get_token(self):
        """
        Ensure Get request return value
        :return:
        """
        token = Token.objects.get(user__username=self.username)
        self.assertTrue(token)
