from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from django.utils import timezone
from user.models import Profile
from .models import Room, Detail
from .permissions import CustomReadOnly
from .serializers import DetailCreateSerializer, DetailSerializer, RoomCreateSerializer, RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == "list" or "retrieve":
            return RoomSerializer
        return RoomCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        end_time = timezone.now()
        serializer.save(user=self.request.user, profile=profile, end_time=end_time)
        return serializer
        
class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action== "list" or "retrieve":
            return DetailSerializer
        return DetailCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        end_focus = timezone.now()
        durations = end_focus - self.request.start_focus
        serializer.save(user=self.request.user, profile=profile, duration=durations, end_focus=end_focus)
        return serializer