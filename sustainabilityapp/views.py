from django.core.exceptions import FieldError
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from knox.auth import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .permissions import *
from . import filters
from . import models


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [filters.OwnerFilter,SearchFilter,DjangoFilterBackend,OrderingFilter]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationPostViewSet(viewsets.ModelViewSet):
    queryset = models.DonationPost.objects.all()
    serializer_class = DonationPostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [filters.OwnerFilter,SearchFilter,DjangoFilterBackend,OrderingFilter]
    def perform_create(self, serializer):
        serializer.save(profile=models.Profile.objects.get(user=self.request.user))

class EventPostViewSet(viewsets.ModelViewSet):
    queryset = models.EventPost.objects.all()
    serializer_class = EventPostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [filters.OwnerFilter,SearchFilter,DjangoFilterBackend,OrderingFilter]
    def perform_create(self, serializer):
        serializer.save(profile=models.Profile.objects.get(user=self.request.user))

"""
class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [filters.OwnerFilter,SearchFilter,DjangoFilterBackend,OrderingFilter]
"""