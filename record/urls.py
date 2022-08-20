from django.urls import path
from rest_framework import routers

from .views import PartyViewSet, DetailViewSet

router = routers.SimpleRouter()
router.register('parties', PartyViewSet)
router.register('details', DetailViewSet)

urlpatterns = router.urls