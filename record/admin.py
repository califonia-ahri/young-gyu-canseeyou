from django.contrib import admin

# Register your models here.
from .models import Party, Detail

admin.site.register(Party)
admin.site.register(Detail)