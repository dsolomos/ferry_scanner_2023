from django.db import models

# Create your models here.

class FerryOption(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    seat_type = models.CharField(max_length=100)
    availability = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'{self.departure} to {self.destination} - {self.date}'
