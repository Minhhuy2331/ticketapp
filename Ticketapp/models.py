from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to='users/%Y/%m')


class ModelBase(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Busroutes(ModelBase):
    point_of_departure = models.CharField(max_length=20, unique=False)
    destination = models.CharField(max_length=20, unique=False)
    pricelist = models.IntegerField()

    def __str__(self):
        return self.name


class Bus(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Busroutes = models.ForeignKey(Busroutes, null=True, related_name='bus', related_query_name='my_bus', on_delete = models.CASCADE)
    booking_date = models.DateField(auto_now_add=True, null=True)


class Range_of_vehicle(models.Model):
    name = models.CharField(max_length=30, unique=False)

    def __str__(self):
        return self.name


class Car(ModelBase):
    license_plate = models.CharField(max_length=15, unique=True) #biển số xe
    number_of_seats = models.IntegerField()
    range_of_vehicle = models.ForeignKey(Range_of_vehicle, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Ticket_details(models.Model):
    seats = models.CharField(max_length=4)
    note = models.CharField(max_length=50)
    bus = models.ForeignKey(Bus, null=True, on_delete=models.SET_NULL)
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, unique=False, on_delete=models.SET_NULL)


class Comment(models.Model):
    content = models.TextField()
    Ticket_details = models.ForeignKey(Ticket_details, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
