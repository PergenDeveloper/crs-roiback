from rest_framework import generics, status
from rest_framework.response import Response

from core.bookings.models import Hotel
from core.bookings.serializers.hotels import HotelSerializer


class HotelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def list(self, request, *args, **kwargs):
        hotel_ids = self.queryset.values_list('code', flat=True)
        return Response(
            data=hotel_ids, status=status.HTTP_200_OK
        )


class HotelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'code'
