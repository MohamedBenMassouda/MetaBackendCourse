from django.db import models


# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name} : {self.date} : {self.time}'
