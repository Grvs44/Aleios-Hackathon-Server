from rest_framework.filters import BaseFilterBackend
from . import models


class OwnerFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset#.filter(id=request.user.id)


class PostOwnerFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
