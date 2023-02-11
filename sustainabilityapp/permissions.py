from rest_framework.permissions import *


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner.user == request.user


class IsImageOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.post.owner.user == request.user


class IsCommentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner.user == request.user
