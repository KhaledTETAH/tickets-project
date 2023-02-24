from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TicketStatusViewSet, TicketViewSet, TicketAssignmentViewSet, NotificationViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ticketStatuses', TicketStatusViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'thicketAssignments', TicketAssignmentViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]