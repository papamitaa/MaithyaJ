from django.db import models

from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.flight_number

class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    flight = models.ForeignKey(Flight, related_name="passengers", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

