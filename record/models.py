from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile

class Room(models.Model):
    RID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='room')
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(auto_now_add=True)
    
class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='detail')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='detail')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='detail')
    focus = models.BooleanField(default=True)
    duration = models.DurationField(blank=True)
    start_focus = models.DateField(auto_now_add=True)
    end_focus = models.DateField(auto_now=True)

