from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=128, null=True)
    photo_tempo = models.IntegerField(default=10)
    notification = models.BooleanField(default=True)
    noti_tempo = models.IntegerField(default=10)
    image = models.ImageField(upload_to='profile/', default='/media/default.png')
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance) 