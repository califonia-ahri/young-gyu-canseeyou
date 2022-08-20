from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include('user.urls')),
    path("records/", include('record.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
