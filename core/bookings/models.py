import uuid as uuid_lib
from django.db import models


class Hotel(models.Model):
    code = models.CharField(max_length=200, unique=True, db_index=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.code}'


class Room(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        related_name='rooms',
        on_delete=models.CASCADE
    )
    code = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.code}'


class Rate(models.Model):
    room = models.ForeignKey(
        Room,
        related_name="rates",
        on_delete=models.CASCADE
    )
    code = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.code}'


class Inventory(models.Model):
    rate = models.ForeignKey(
        Rate,
        related_name="inventories",
        on_delete=models.CASCADE
    )
    date = models.DateField(db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    allotment = models.PositiveIntegerField(default=0, db_index=True)
    uuid = models.UUIDField(
        unique=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    class Meta:
        unique_together = ('rate', 'date')
