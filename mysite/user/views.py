from django.contrib.auth.models import User
from .models import Profile
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from record.models import Room, Detail
from .utils import get_turn_info
from record.serializers import DetailSerializer
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, SettingSerializer
from .permissions import CustomReadOnly


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def get(self,request):
        return render(request, 'user/register.html')
    
    def post(self, request):
        return redirect('login_view')

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def get(self,request):
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
    
    def view(request):
        if request.method == 'POST':
                data = request.payload
                # do something
                print(data)

                context = {
                    'result': data,
                }
                return context    


 

class SettingView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [CustomReadOnly]
    serializer_class = SettingSerializer
    
    def get(self, request):
        return render(request, 'user/setting.html')
    
class StatisView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    permission_classes = [CustomReadOnly]
    serializer_class = DetailSerializer

    def get(self, request):
        return render(request, 'record/statics.html')


def view(request):
   if request.method == 'POST':
        data = request.body
        # do something
        print(data)

        context = {
            'result': data,
        }
        return context