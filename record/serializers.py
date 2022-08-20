from rest_framework import serializers

from user.serializers import ProfileSerializer
from .models import Party, Detail

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ("pid","user", "start_focus", "end_focus")
    
    def to_representation(self, instance):
        self.fields['pid'] = PartyRepresentationSerializer(read_only=True)
        return super(DetailSerializer, self).to_representation(instance)

class DetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ("user", "start_focus", "end_focus")

class PartySerializer(serializers.ModelSerializer):
    detail = DetailSerializer(read_only=True, many=True)
    class Meta:
        model = Party
        fields = ("PID", "user", "start_time", "end_time", "detail")
        
class PartyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ("user", "start_time", "end_time")

class PartyRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ("PID", )