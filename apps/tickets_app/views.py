from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import TicketStatus, Ticket, Notification
from .serializers import UserSerializer, TicketSerializer, NotificationSerializer, TicketStatusSerializer, NotificationSerializerForGetTickets
from django.http import FileResponse
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TicketStatusViewSet(viewsets.ModelViewSet):
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer
    
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-id')
    serializer_class = TicketSerializer
    
    
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
  
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_user_by_username(request, username):
    try:
        user = User.objects.filter(username=username).first()
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def get_notification_by_user(request, userId):
    try:
        notifs = Notification.objects.filter(notified_user=userId)
        print("#############################")
        print(notifs)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = NotificationSerializer(notifs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def download_file(request):
    file_path = request.query_params.get('file_path')
    print(file_path)
    file_path = file_path.replace("%2F","/")
    pattern = "media/uploads"
    start_index = file_path.find(pattern)  # Find the starting index of the pattern
    if start_index != -1:  # If the pattern is found
        substring = file_path[start_index:]  # Extract substring from the starting index
        print(substring)  # Output: world
    else:
        print("Pattern not found")
    return FileResponse(open(substring, 'rb'))


@api_view(['GET'])
def get_notification_ticket_details(request, notifiedUserId):
    try:
        notif = Notification.objects.filter(notified_user=notifiedUserId).order_by('-time')
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = NotificationSerializerForGetTickets(notif, many=True)
    return Response(serializer.data)