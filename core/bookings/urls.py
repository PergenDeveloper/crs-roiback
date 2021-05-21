from django.urls import path, re_path
from core.bookings.views import hotels as hotel_views
from core.bookings.views import rooms as room_views
from core.bookings.views import rates as rate_views
from core.bookings.views import inventories as inventory_views
from core.bookings.views import commons as commons_views

urlpatterns = [
    # Hotels urls
    path('hotels/', hotel_views.HotelListCreateAPIView.as_view(), name='hotel-list-create'),
    path('hotels/<str:code>/',
         hotel_views.HotelRetrieveUpdateDestroyAPIView.as_view(),
         name='hotel-retrieve-update-destroy'),

    # Rooms urls
    path('rooms/', room_views.RoomListCreateAPIView.as_view(), name='room-list-create'),
    path('rooms/<str:code>/',
         room_views.RoomRetrieveUpdateDestroyAPIView.as_view(),
         name='room-retrieve-update-destroy'),

    # Rates urls
    path('rates/', rate_views.RateListCreateAPIView.as_view(), name='rate-list-create'),
    path('rates/<str:code>/',
         rate_views.RateRetrieveUpdateDestroyAPIView.as_view(),
         name='rate-retrieve-update-destroy'),

    # Inventory urls
    path('inventories/', inventory_views.InventoryListCreateAPIView.as_view(), name='inventory-list-create'),
    path('inventories/<str:uuid>/',
         inventory_views.InventoryRetrieveUpdateDestroyAPIView.as_view(),
         name='inventory-retrieve-update-destroy'),

    # Commons urls
    re_path(
        r'^availability/(?P<hotel_code>\w+)/'
        r'(?P<checkin_date>\d{4}-\d{2}-\d{2})/'
        r'(?P<checkout_date>\d{4}-\d{2}-\d{2})/$',
        commons_views.AvailabilityAPIView.as_view(),
        name='availability'
    )
]
