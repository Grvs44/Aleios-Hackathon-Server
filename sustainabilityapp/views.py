from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
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

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [filters.OwnerFilter,SearchFilter,DjangoFilterBackend,OrderingFilter]
    def perform_create(self, serializer):
        serializer.save(profile=models.Profile.objects.get(user=self.request.user))



class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [filters.OwnerFilter,SearchFilter,DjangoFilterBackend,OrderingFilter]

"""
class SignUpView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            profile = models.Profile(user=user)
            profile.save()
            return Response({'detail': 'Created user'})
        except KeyError:
            return Response({'detail': 'Username and password are required'}, 400)
"""

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
