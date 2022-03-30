from orderProducts.models import Order
from orderProducts.serializers import OrderSerializers
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


from orderProducts.utils import ProductAvailability


class OrderView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user_id=user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            request.data['user'] = request.user.id
            return self.create(request, *args, **kwargs)
        except ProductAvailability as message:
            raise APIException(message)
