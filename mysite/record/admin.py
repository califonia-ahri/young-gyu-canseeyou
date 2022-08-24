from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Room, Detail

admin.site.register(Room)
admin.site.register(Detail)
