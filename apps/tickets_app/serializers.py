from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TicketStatus, Ticket, TicketAssignment, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    #created_by = UserSerializer()
    class Meta:
        model = Ticket
        fields = '__all__'
        
class TicketAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAssignment
        fields = '__all__'
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'