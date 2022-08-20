from django.shortcuts import render

from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from django.utils import timezone
from user.models import Profile
from .models import Party, Detail
from .permissions import CustomReadOnly
from .serializers import DetailCreateSerializer, DetailSerializer, PartyCreateSerializer, PartySerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == "list" or "retrieve":
            return PartySerializer
        return PartyCreateSerializer
    
    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)
    
    def update(self, serializer):
        end_time = timezone.now()
        serializer.save(user=self.request.user, end_time=end_time)


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action== "list" or "retrieve":
            return DetailSerializer
        return DetailCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def update(self, serializer):
        end_focus = timezone.now()
        serializer.save(end_focus=end_focus)