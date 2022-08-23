from django.urls import path
from rest_framework import routers

from .views import RoomViewSet, DetailViewSet, StatisViewSet

router = routers.SimpleRouter()
router.register('rooms', RoomViewSet)
router.register('details', DetailViewSet)

urlpatterns = [
    
]
