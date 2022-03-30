from products.models import Product
from products.serializers import ProductSerializers
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication


class ProductList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)