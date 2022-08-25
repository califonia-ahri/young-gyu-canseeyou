from rest_framework import serializers

from user.serializers import ProfileSerializer
from .models import Room, Detail

class DetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = Detail
        fields = ("RID", "profile", "duration", "start_focus", "end_focus", "focus_date")

class DetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail

class RoomSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    detail = DetailSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        field = ("RID", "profile", "start_time", "end_time", "detail", "start_date")
        
class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room