from rest_framework.permissions import *


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        else:
            return obj == request.user


class IsPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        else:
            return obj.owner.user == request.user


class IsImageOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        else:
            return obj.post.owner.user == request.user


class IsCommentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        else:
            return obj.owner.user == request.user
