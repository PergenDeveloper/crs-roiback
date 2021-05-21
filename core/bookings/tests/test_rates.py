import pytest

from django.urls import reverse

from core.bookings.models import Hotel, Room, Rate


@pytest.mark.django_db
def test_create_rate(client):
    hotel = Hotel.objects.create(
        code="hotel_1",
        name="Hotel 1"
    )
    room = Room.objects.create(
        hotel=hotel,
        code="room_1",
        name="Room 1"
    )

    url = reverse('rate-list-create')
    response = client.post(url, {
        "room": room.code,
        "code": "rate_1",
        "name": "Premium"
    })

    assert Rate.objects.count() > 0
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_rate(client):
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

    url = reverse('rate-retrieve-update-destroy', kwargs={"code": rate.code})
    response = client.patch(url, {
        "name": "Basic"
    }, content_type='application/json')

    rate_updated = Rate.objects.get(code=rate.code)

    assert rate_updated.name == "Basic"
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_rate(client):
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

    url = reverse('rate-retrieve-update-destroy', kwargs={"code": rate.code})
    response = client.delete(url)

    assert not Rate.objects.filter(code="rate_1").exists()
    assert response.status_code == 204
