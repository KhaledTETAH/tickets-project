from django.db import models
from django.utils import timezone

# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(primary_key=False, max_length=150)
    description = models.TextField(primary_key=False)
    deadline = models.DateTimeField(primary_key=False)
    
class Assistant(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    firstname = models.CharField(primary_key=False, max_length=150)
    lastname = models.CharField(primary_key=False, max_length=150)
    class Meta:
        abstract = True

class AssistantFr(Assistant):
    poste = models.CharField(max_length=2, default='FR')

class AssistantDz(Assistant):
    poste = models.CharField(max_length=2, default='DZ')
    
class TicketStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(primary_key=False, max_length=50)

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(primary_key=False, default=timezone.now)