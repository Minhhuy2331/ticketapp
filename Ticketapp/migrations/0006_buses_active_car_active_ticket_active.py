# Generated by Django 4.0.2 on 2022-05-18 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketapp', '0005_remove_buses_active_remove_car_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buses',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='car',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
