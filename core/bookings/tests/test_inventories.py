from decimal import Decimal

import pytest

from django.urls import reverse

from core.bookings.models import Hotel, Room, Rate, Inventory


@pytest.mark.django_db
def test_create_inventory(client):
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

    url = reverse('inventory-list-create')
    response = client.post(url, {
        "rate": rate.code,
        "date": "2021-05-24",
        "price": 63.35,
        "allotment": 3
    })

    assert Inventory.objects.count() > 0
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_inventory(client):
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
    inventory = Inventory.objects.create(
        rate=rate,
        date="2021-05-24",
        price=74.56,
        allotment=2
    )

    url = reverse('inventory-retrieve-update-destroy', kwargs={"uuid": inventory.uuid.hex})
    response = client.patch(url, {
        "price": 46.80
    }, content_type='application/json')

    inventory_updated = Inventory.objects.get(uuid=inventory.uuid)

    assert inventory_updated.price == Decimal('46.80')
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_inventory(client):
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
    inventory = Inventory.objects.create(
        rate=rate,
        date="2021-05-24",
        price=74.56,
        allotment=2
    )

    url = reverse('inventory-retrieve-update-destroy', kwargs={"uuid": inventory.uuid.hex})
    response = client.delete(url)

    assert not Inventory.objects.filter(uuid=inventory.uuid).exists()
    assert response.status_code == 204


@pytest.mark.django_db
def test_inventory_rate_same_day(client):
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

    url = reverse('inventory-list-create')
    response = client.post(url, {
        "rate": rate.code,
        "date": "2021-05-24",
        "price": 63.35,
        "allotment": 1
    })

    assert response.status_code == 400
