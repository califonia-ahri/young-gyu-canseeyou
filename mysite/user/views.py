import py_compile
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
from ml import test2

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
        
        
    
class StatisView(generics.GenericAPIView):
    queryset = Room.objects.all()
    permission_classes = [CustomReadOnly]
    serializer_class = DetailSerializer

    def get(self, request):
        user = User.objects.get(auth_token=request.COOKIES.get('token'))
        rooms = Room.objects.filter(user=user, start_time__gte=datetime.today(),
                                start_time__lte=datetime.today() + timedelta(days=1))
        details = Detail.objects.filter(user=user, start_focus__gte=datetime.today(),
                                        start_focus__lte=datetime.today()+timedelta(days=1))
        room_hour = 0
        room_min = 0
        detail_hour = 0
        detail_min = 0
        
        for room in rooms:
            room_hour += (room.end_time - room.start_time).seconds // 3600
            room_min += ((room.end_time - room.start_time).seconds % 3600) // 60
        
        for detail in details:
            detail_hour += (detail.end_focus - detail.start_focus).seconds // 3600
            detail_min += ((detail.end_focus - detail.start_focus).seconds%3600)//60
        
        return render(request, 'record/statics.html', {"room_hour":room_hour, "room_min":room_min,  
                                                       "detail_hour":detail_hour, "detail_min":detail_min})
    
    def post(self, request):
        user = User.objects.get(auth_token=request.COOKIES.get('token'))
        rooms = Room.objects.filter(user=user, start_time__gte=datetime(int(request.POST['year']), int(request.POST['month']), int(request.POST['date'])),
                                start_time__lte=datetime(int(request.POST['year']), int(request.POST['month']), int(request.POST['date'])+1))
        details = Detail.objects.filter(user=user, start_focus__gte=datetime(int(request.POST['year']), int(request.POST['month']), int(request.POST['date'])),
                                start_focus__lte=datetime(int(request.POST['year']), int(request.POST['month']), int(request.POST['date'])+1))
        room_hour = 0
        room_min = 0
        detail_hour = 0
        detail_min = 0
        
        for room in rooms:
            room_hour += (room.end_time - room.start_time).seconds // 3600
            room_min += ((room.end_time - room.start_time).seconds % 3600) // 60
        
        for detail in details:
            detail_hour += (detail.end_focus - detail.start_focus).seconds // 3600
            detail_min += ((detail.end_focus - detail.start_focus).seconds%3600)//60
        
        return render(request, 'record/statics.html', {"room_hour":room_hour, "room_min":room_min,  
                                                       "detail_hour":detail_hour, "detail_min":detail_min,
                "rooms":rooms, "details":details})

class TestView(generics.GenericAPIView):
    
    def get(self, request):
        # test2.starting()
        return render(request, 'home_view')