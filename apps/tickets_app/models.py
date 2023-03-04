from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class TicketStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
class Ticket(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(User,related_name='created_by', null=True, on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='assigned_to')
    assigned_on = models.DateTimeField(null=True)
    feedback = models.FileField(upload_to='uploads/', null=True, blank=True, unique=True)
    remarks = models.TextField(null=True, blank=True)
    status = models.ForeignKey(TicketStatus, related_name='ticket_status', on_delete=models.CASCADE)
    
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(default=timezone.now)
    by_ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    ticket_status = models.IntegerField(default=0)
    notified_user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)