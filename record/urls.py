from django.urls import path
from rest_framework import routers

from .views import RoomViewSet, DetailViewSet

router = routers.SimpleRouter()
router.register('rooms', RoomViewSet)
router.register('details', DetailViewSet)
