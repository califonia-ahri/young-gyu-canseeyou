from django.contrib.auth.models import User
from .models import Profile
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, SettingSerializer
from .permissions import CustomReadOnly

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        token = serializer.validated_data
        return Response({"token":token.key}, status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class SettingsView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [CustomReadOnly]
    serializer_class = SettingSerializer