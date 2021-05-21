import pytest

from django.urls import reverse

from core.bookings.models import Hotel, Room


@pytest.mark.django_db
def test_room_belong_to_only_one_hotel(client):
    hotel = Hotel.objects.create(code="hotel_1", name="Hotel 1")
    room = Room.objects.create(hotel=hotel, code="room_1", name="Room 1")

    url = reverse('room-list-create')
    response = client.post(url, {
        "hotel": hotel.code,
        "code": room.code,
        "name": "Room 1"
    })

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_room(client):
    hotel = Hotel.objects.create(code="hotel_1", name="Hotel 1")
    url = reverse('room-list-create')
    response = client.post(url, {
        "hotel": hotel.code,
        "code": "room_1",
        "name": "Hotel 1 Replica"
    })

    assert Room.objects.count() > 0
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_room(client):
    hotel_1 = Hotel.objects.create(
        code="hotel_1",
        name="Hotel 1"
    )
    hotel_2 = Hotel.objects.create(
        code="hotel_2",
        name="Hotel 1"
    )
    room = Room.objects.create(
        hotel=hotel_1,
        code="room_1",
        name="Room 1"
    )

    url = reverse('room-retrieve-update-destroy', kwargs={"code": room.code})
    response = client.patch(url, {
        "hotel": hotel_2.code
    }, content_type='application/json')

    room_updated = Room.objects.get(code=room.code)

    assert room_updated.hotel.code == "hotel_2"
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_room(client):
    hotel = Hotel.objects.create(
        code="hotel_1",
        name="Hotel 1"
    )
    room = Room.objects.create(
        hotel=hotel,
        code="room_1",
        name="Room 1"
    )

    url = reverse('room-retrieve-update-destroy', kwargs={"code": room.code})
    response = client.delete(url)

    assert not Room.objects.filter(code="room_1").exists()
    assert response.status_code == 204
