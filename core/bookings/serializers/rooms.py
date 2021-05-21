from rest_framework import serializers

from core.bookings.models import Hotel, Room


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.SlugRelatedField(
        read_only=False,
        queryset=Hotel.objects.all(),
        slug_field='code'
    )

    class Meta:
        model = Room
        fields = ('hotel', 'code', 'name')
