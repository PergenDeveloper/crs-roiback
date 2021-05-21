import pytest

from django.urls import reverse

from core.bookings.models import Hotel


@pytest.mark.django_db
def test_unique_code_in_hotel(client):
    Hotel.objects.create(code="hotel_1", name="Hotel 1")

    url = reverse('hotel-list-create')
    response = client.post(url, {
        "code": "hotel_1",
        "name": "Hotel 1 Replica"
    })

    assert response.status_code == 400


@pytest.mark.django_db
def test_check_hotel_name_in_list(client):
    hotel = Hotel.objects.create(code="hotel_1", name="Hotel 1")

    url = reverse('hotel-list-create')
    response = client.get(url)
    data = response.json()

    assert hotel.code in data["hotels"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_hotel(client):
    url = reverse('hotel-list-create')
    response = client.post(url, {
        "code": "hotel_1",
        "name": "Hotel 1 Replica"
    })

    assert Hotel.objects.count() > 0
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_hotel(client):
    hotel = Hotel.objects.create(code="hotel_1", name="Hotel 1")

    url = reverse('hotel-retrieve-update-destroy', kwargs={"code": hotel.code})
    response = client.patch(url, {
        "name": "Hotel updated"
    }, content_type='application/json')

    hotel_updated = Hotel.objects.get(code="hotel_1")

    assert hotel.name == "Hotel 1"
    assert hotel_updated.name == "Hotel updated"
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_hotel(client):
    hotel = Hotel.objects.create(code="hotel_1", name="Hotel 1")

    url = reverse('hotel-retrieve-update-destroy', kwargs={"code": hotel.code})
    response = client.delete(url)

    assert not Hotel.objects.filter(code="hotel_1").exists()
    assert response.status_code == 204
