from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile

class Room(models.Model):
    RID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room', null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='room', null=True)
    start_date = models.DateField(auto_now_add=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.start_date
    
class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='detail', null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='detail', null=True)
    focus_date = models.DateField(auto_now_add=True)
    start_focus = models.DateTimeField(auto_now_add=True)
    end_focus = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.focus_date