from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .models import Profile
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from record.models import Room, Detail

from record.serializers import DetailSerializer
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, SettingSerializer
from .permissions import CustomReadOnly
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
        
    def get(self, request):
        return render(request, 'user/register.html')
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login_view')
        

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    template_name = 'user/login.html'
    
    def get(self, request):
        return render(request, 'user/login.html')
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = serializer.validated_data
            return render(request,"user/home.html", {"token":token.key})
        else:
            return redirect('login_view')

class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get(self, request):
        return render(request, 'user/home.html', {'user':request.user})

class SettingView(generics.GenericAPIView):
    queryset = Profile.objects.all()
    permission_classes = [CustomReadOnly]
    serializer_class = SettingSerializer
    
    def get(self, request):
        return render(request, 'user/setting.html')
    def post(self, serializer):
        profile = Profile.objects.get_object_or_404(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)
    
class StatisView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    permission_classes = [CustomReadOnly]
    serializer_class = DetailSerializer

    def get(self, request):
        return render(request, 'record/statics.html')