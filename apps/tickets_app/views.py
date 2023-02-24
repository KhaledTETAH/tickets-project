from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import TicketStatus, Ticket, TicketAssignment, Notification
from .serializers import UserSerializer, TicketAssignmentSerializer, TicketSerializer, NotificationSerializer, TicketStatusSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TicketStatusViewSet(viewsets.ModelViewSet):
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer
    
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
class TicketAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TicketAssignment.objects.all()
    serializer_class = TicketAssignmentSerializer
    
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer