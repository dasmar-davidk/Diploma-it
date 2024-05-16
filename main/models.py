from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    payment_method = models.CharField(max_length=100)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    massage = models.TextField()