from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile

class Room(models.Model):
    RID = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(auto_now_add=True)
    
class Detail(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='detail')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='detail')
    focus = models.BooleanField(default=True)
    duration = models.DurationField(blank=True)
    start_focus = models.DateField(auto_now_add=True)
    end_focus = models.DateField(auto_now_add=True)

