from rest_framework import serializers

from core.bookings.models import Rate, Inventory


class InventorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source='uuid',
        format='hex',
        read_only=True
    )
    rate = serializers.SlugRelatedField(
        read_only=False,
        queryset=Rate.objects.all(),
        slug_field='code'
    )

    class Meta:
        model = Inventory
        fields = ['id', 'rate', 'date', 'price', 'allotment']
