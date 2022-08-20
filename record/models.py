from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile

class Party(models.Model):
    PID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room', null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    
    
class Detail(models.Model):
    pid = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='detail', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='detail', null=True)
    start_focus = models.DateTimeField(auto_now_add=True)
    end_focus = models.DateTimeField(auto_now=True)