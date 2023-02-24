from django.contrib import admin
from apps.tickets_app.models import AssistantDz, AssistantFr, Notification, Ticket, TicketStatus

# Register your models here.
models = [Ticket, AssistantFr, AssistantDz, TicketStatus, Notification]
for model in models:
    admin.site.register(model)