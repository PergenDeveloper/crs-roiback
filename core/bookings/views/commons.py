from itertools import groupby
from decimal import Decimal

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.bookings.models import Inventory


class AvailabilityAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = self.get_available_rooms()
        return Response(data=data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Inventory.objects.select_related('rate__room').filter(
            date__gte=self.kwargs.get('checkin_date'),
            date__lte=self.kwargs.get('checkout_date'),
            allotment__gt=0,
            rate__room__hotel__code=self.kwargs.get('hotel_code')
        ).order_by('rate__room__code', 'rate__code', 'date')
        return queryset

    def get_available_rooms(self):
        rooms = []
        queryset = self.get_queryset()
        for room_code, group_by_room in groupby(queryset, lambda x: x.rate.room.code):
            rates = self.get_rates_per_room(group_by_room)
            rooms.append({
                room_code: {
                    "rates": rates
                }
            })
        return {'rooms': rooms}

    def get_rates_per_room(self, group):
        rates = []
        for rate_code, group_by_rate in groupby(group, lambda x: x.rate.code):
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

    def get_inventories_and_total_price_per_rate(self, group):
        inventories, total_price = {}, Decimal()
        for item in group:
            total_price += item.price
            inventories[str(item.date)] = {
                "price": item.price,
                "allotment": item.allotment
            }
        return inventories, total_price
