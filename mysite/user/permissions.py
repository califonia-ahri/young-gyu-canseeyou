from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.meth in permissions.SAFE_METHODS:
            return True
        return obj.user==request.user