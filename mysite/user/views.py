from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .models import Profile
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from record.models import Room, Detail
from django.views.generic import UpdateView

from record.serializers import DetailSerializer
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, SettingSerializer
from .permissions import CustomReadOnly
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta

class RegisterView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
        
    def get(self, request):
        return render(request, 'user/register.html')
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login_view')
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    template_name = 'user/login.html'
    
    def get(self, request):
        return render(request, 'user/login.html')
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = serializer.validated_data
            response = redirect('home_view')
            response.set_cookie('token', token.key)
            return response
        else:
            return redirect('login_view')

class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get(self, request):
        user = User.objects.get(auth_token=request.COOKIES.get('token'))
        profile = Profile.objects.get_or_create(user=user)
        return render(request, 'user/home.html', {'users':profile})

class SettingView(generics.GenericAPIView, UpdateView):
    queryset = Profile.objects.all()
    permission_classes = [CustomReadOnly]
    serializer_class = SettingSerializer
    
    def get(self, request):
        user = User.objects.get(auth_token=request.COOKIES.get('token'))
        profile = Profile.objects.get_or_create(user=user)
        return render(request, 'user/setting.html', {"users":profile})
    
    def post(self,request):
        user = User.objects.get(auth_token=request.COOKIES.get('token'))
        profile = Profile.objects.get(user=user)
        
        serializer =  SettingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            profile.nickname = serializer.data['nickname']
            profile.photo_tempo = serializer.data['photo_tempo']
            profile.notification = serializer.data['notification']
            profile.noti_tempo = serializer.data['noti_tempo']
            profile.save()
        
        profile = Profile.objects.filter(user=user)
        return render(request, 'user/setting.html', {"users":profile})
        
        
    
class StatisView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    permission_classes = [CustomReadOnly]
    serializer_class = DetailSerializer

    def get(self, request):
        # user = User.objects.get(auth_token=request.COOKIES.get('token'))
        # rooms = Room.objects.filter(user=user, start_time=request.GET.get('start_time'))
        # details = Detail.objects.filter(user=user, start_time=request.GET.get('start_time'))
        # room_time = datetime(0,0,0,0,0,0)
        # detail_time = datetime(0,0,0,0,0,0)
        
        # for room in rooms:
        #     room_time += (room.end_time - room.start_time)
        
        # for detail in details:
        #     detail_time += (detail.end_focus - detail.start_focus)
        
        return render(request, 'record/statics.html')
    
    def post(self, request):
        user = User.objects.get(auth_token=request.COOKIES.get('token'))
        now = datetime(request.POST['year'], request.POST['month'], request.POST['date'])
        rooms = Room.objects.filter(user=user, start_time=now)
        details = Detail.objects.filter(user=user, start_focus=now)
        room_time = datetime(0,0,0,0,0,0)
        detail_time = datetime(0,0,0,0,0,0)
        
        for room in rooms:
            room_time += (room.end_time - room.start_time)
        
        for detail in details:
            detail_time += (detail.end_focus - detail.start_focus)
        
        return render(request, 'record/statics.html', {"room_time":room_time, "detail_time":detail_time})