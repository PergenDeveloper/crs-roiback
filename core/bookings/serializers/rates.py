from rest_framework import serializers

from core.bookings.models import Room, Rate


class RateSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField(
        read_only=False,
        queryset=Room.objects.all(),
        slug_field='code'
    )

    class Meta:
        model = Rate
        fields = ['room', 'code', 'name']
