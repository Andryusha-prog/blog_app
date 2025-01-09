from rest_framework.permissions import BasePermission


class IsAdmins(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Admins").exists()


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsOwnerPost(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsOwnerComment(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
