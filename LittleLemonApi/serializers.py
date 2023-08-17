import rest_framework.serializers
from .models import MenuItem, Booking


class MenuItemSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class BookingSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
