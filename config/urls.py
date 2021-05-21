from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/inventories/', include('crsystem.inventories.urls')),
    path('api/', include('core.bookings.urls')),
]
