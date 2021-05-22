import pytest

from django.urls import reverse

from core.bookings.models import Hotel, Room, Rate, Inventory


@pytest.mark.django_db
def test_availability_not_found_between_dates(client):
    hotel = Hotel.objects.create(
        code="hotel_1",
        name="Hotel 1"
    )
    room = Room.objects.create(
        hotel=hotel,
        code="room_1",
        name="Room 1"
    )
    rate = Rate.objects.create(
        room=room,
        code="rate_1",
        name="Premium"
    )
    Inventory.objects.create(
        rate=rate,
        date="2021-05-24",
        price=74.56,
        allotment=2
    )

    url = reverse('availability', kwargs={
        "hotel_code": hotel.code,
        "checkin_date": "2021-02-02",
        "checkout_date": "2021-03-22"
    })
    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_availability_not_found_in_hotel(client):
    hotel_1 = Hotel.objects.create(
        code="hotel_1",
        name="Hotel 1"
    )
    hotel_2 = Hotel.objects.create(
        code="hotel_2",
        name="Hotel 2"
    )

    room = Room.objects.create(
        hotel=hotel_1,
        code="room_1",
        name="Room 1"
    )
    rate = Rate.objects.create(
        room=room,
        code="rate_1",
        name="Premium"
    )
    Inventory.objects.create(
        rate=rate,
        date="2021-05-24",
        price=74.56,
        allotment=2
    )

    url = reverse('availability', kwargs={
        "hotel_code": hotel_2.code,
        "checkin_date": "2021-05-23",
        "checkout_date": "2021-05-25"
    })
    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_availability_found(client):
    hotel = Hotel.objects.create(
        code="hotel_1",
        name="Hotel 1"
    )

    room = Room.objects.create(
        hotel=hotel,
        code="room_1",
        name="Room 1"
    )
    rate = Rate.objects.create(
        room=room,
        code="rate_1",
        name="Premium"
    )
    Inventory.objects.create(
        rate=rate,
        date="2021-05-24",
        price=74.56,
        allotment=2
    )

    url = reverse('availability', kwargs={
        "hotel_code": hotel.code,
        "checkin_date": "2021-05-23",
        "checkout_date": "2021-05-25"
    })
    response = client.get(url)
    data = response.json()

    assert room.code in data["rooms"][0]
    assert rate.code in data["rooms"][0][room.code]['rates'][0]
    assert response.status_code == 200
