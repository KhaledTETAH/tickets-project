from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TicketStatus, Ticket, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
#    created_by = UserSerializer()
#    status = TicketStatusSerializer()
    class Meta:
        model = Ticket
        fields = '__all__'
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        

class NotificationSerializerForGetTickets(serializers.ModelSerializer):
    by_ticket = TicketSerializer()
    class Meta:
        model = Notification
        fields = '__all__'