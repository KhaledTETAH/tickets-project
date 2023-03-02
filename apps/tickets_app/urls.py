from django.urls import path, include
from rest_framework import routers
from . import views
from .views import UserViewSet, TicketStatusViewSet, TicketViewSet, NotificationViewSet, get_notification_ticket_details

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ticketStatuses', TicketStatusViewSet)
router.register(r'tickets', TicketViewSet)
#router.register(r'thicketAssignments', TicketAssignmentViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/username/<str:username>', views.get_user_by_username),
    path('file/download/', views.download_file),
    path('notifications/user/<int:userId>', views.get_notification_by_user),
    path('notifications/ticket/details/<int:notifiedUserId>', views.get_notification_ticket_details),
]