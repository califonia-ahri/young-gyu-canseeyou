from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())],    # block overlapped email
        required = True
    )
    
    password = serializers.CharField(
        help_text="password input",
        write_only = True,
        validators=[validate_password],
        required = True
    )
    
    password2 = serializers.CharField(write_only=True, required=True)   # for password checking
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self,data):                                            # testing password validity
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match."}
            )
        return data
    
    def create(self, request, validated_data):               # override create method and create user and token
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)    # prevent server -> client deserialization

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error":"Unable to log in with provided credentials."}
        )
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nickname", "image")
        
class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("photo_tempo", "noti_tempo", "notification", "image")