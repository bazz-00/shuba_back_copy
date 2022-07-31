from rest_framework import serializers

from .models import Order, OrderComments, OrderPhotos, SpecialityOrder
from user.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    # user = UserSerializer(default=serializers.CurrentUserDefault())
    # date_finish = serializers.DateField('date_finish')

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "title",
            "description",
            "city",
            "name",
            "phoneNumber",
            "price",
            "date_finish",
            "speciality"
        ]

    def create(self, validated_data):
        print(validated_data)
        return super(OrderSerializer, self).create(validated_data)


class SpecialityOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityOrder
        fields = '__all__'


class OrderCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderComments
        fields = '__all__'


class OrderPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPhotos
        fields = '__all__'