from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class TicketStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(primary_key=False, max_length=50)
    
class Ticket(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(User,related_name='created_by', null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(TicketStatus, related_name='ticket_status', on_delete=models.CASCADE)
    
class TicketAssignment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='ticket')
    assigned_to = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='assigned_to')
    assigned_on = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(TicketStatus, null=True, on_delete=models.SET_NULL, related_name='assigned_status')

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(primary_key=False, default=timezone.now)
    ticket = models.ForeignKey(TicketAssignment, on_delete=models.CASCADE)
    notified_user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)