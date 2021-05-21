# Generated by Django 3.2.3 on 2021-05-21 12:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='bookings.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='bookings.room')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('allotment', models.PositiveIntegerField(db_index=True, default=0)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='bookings.rate')),
            ],
            options={
                'unique_together': {('rate', 'date')},
            },
        ),
    ]