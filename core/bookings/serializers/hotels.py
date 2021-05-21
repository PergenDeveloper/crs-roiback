from rest_framework import serializers

from core.bookings.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['code', 'name']
