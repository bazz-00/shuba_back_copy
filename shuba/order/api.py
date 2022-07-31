from .models import Order, OrderComments, OrderPhotos, SpecialityOrder
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer, OrderCommentsSerializer, OrderPhotosSerializer, SpecialityOrderSerializer
from django_filters.rest_framework import DjangoFilterBackend


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['speciality']
    
    # def create(self, request, *args, **kwargs):
    #     # import pdb
    #     # pdb.set_trace()
    #     return super(OrderViewSet, self).create(reqeust, *args)


class SpecialityOrderViewSet(viewsets.ModelViewSet):
    queryset = SpecialityOrder.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SpecialityOrderSerializer



class OrderCommentsViewSet(viewsets.ModelViewSet):
    queryset = OrderComments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderCommentsSerializer


class OrderPhotosViewSet(viewsets.ModelViewSet):
    queryset = OrderPhotos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderPhotosSerializer




