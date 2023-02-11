from rest_framework.filters import BaseFilterBackend
from . import models

class OwnerFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)


class PostOwnerFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset#.filter(owner=models.Profile.objects.get(user=request.user))
