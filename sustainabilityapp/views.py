from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from knox.auth import TokenAuthentication
import knox.views
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from . import permissions
from . import filters
from . import models


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [filters.OwnerFilter,SearchFilter,DjangoFilterBackend,OrderingFilter]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsPostOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [filters.PostOwnerFilter,SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['tags']
    def perform_create(self, serializer):
        serializer.save(profile=models.Profile.objects.get(user=self.request.user))


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsImageOwner]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsCommentOwner]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]


class UserCreateAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class LoginView(knox.views.LoginView):
    def get_post_response_data(self, request, token, instance):
        UserSerializer = self.get_user_serializer_class()
        try:
            profile = models.Profile.objects.get(user=request.user)
        except models.Profile.DoesNotExist:
            profile = models.Profile(user=request.user)
            profile.save()

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token,
            'first_name': request.user.first_name,
            'profile': profile.id,
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data
        return data
