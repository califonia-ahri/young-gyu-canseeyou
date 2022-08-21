from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        return obj.user==request.user