from itertools import groupby
from decimal import Decimal

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.bookings.utils import raise_404_if_empty
from core.bookings.models import Inventory


class AvailabilityAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = self.get_available_rooms()
        return Response(data=data, status=status.HTTP_200_OK)

    @raise_404_if_empty
    def get_queryset(self):
        queryset = Inventory.objects.select_related('rate__room').filter(
            date__gte=self.kwargs.get('checkin_date'),
            date__lte=self.kwargs.get('checkout_date'),
            allotment__gt=0,
            rate__room__hotel__code=self.kwargs.get('hotel_code')
        ).order_by('rate__room__code', 'rate__code', 'date')
        return queryset

    def get_available_rooms(self):
        queryset = self.get_queryset()
        data = self.format_data(queryset)
        return data

    def format_data(self, data):
        rooms = []
        """
        Group the data by room code and get rates per each room
        """
        for room_code, group_by_room in groupby(data, lambda x: x.rate.room.code):
            rates = self.get_rates_per_room(group_by_room)
            rooms.append({
                room_code: {
                    "rates": rates
                }
            })
        return {'rooms': rooms}

    def get_rates_per_room(self, data):
        """
        Group the data by rate code and get inventories and total price per each rate
        """
        rates = []
        for rate_code, group_by_rate in groupby(data, lambda x: x.rate.code):
            inventories, total_price = self.get_inventories_and_total_price_per_rate(group_by_rate)
            rates.append(
                {
                    rate_code: {
                        "total_price": total_price,
                        "breakdown": [
                            inventories
                        ]
                    }
                }
            )
        return rates

    def get_inventories_and_total_price_per_rate(self, data):
        """
        Create a dict of inventories per date and get total price
        """
        inventories, total_price = {}, Decimal()
        for item in data:
            total_price += item.price
            inventories[str(item.date)] = {
                "price": item.price,
                "allotment": item.allotment
            }
        return inventories, total_price
