from django.contrib import admin
from .models import Event, Ticket, Order, Notification

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(Notification)