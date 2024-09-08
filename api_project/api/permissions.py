from rest_framework.permissions import BasePermission

class IsAuthorReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTION"]:
            return True
        return obj.author == request.User