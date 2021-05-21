from rest_framework import generics

from core.bookings.models import Rate
from core.bookings.serializers.rates import RateSerializer


class RateListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    lookup_field = 'code'
