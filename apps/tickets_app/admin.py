from django.contrib import admin
from apps.tickets_app.models import Notification, Ticket, TicketStatus

# Register your models here.
models = [Ticket, TicketStatus,  Notification]
for model in models:
    admin.site.register(model)