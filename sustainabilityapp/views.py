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


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsOwner]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [filters.OwnerFilter, SearchFilter,
                       DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id']


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsPostOwner]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [filters.PostOwnerFilter,
                       SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['tags']


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsImageOwner]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id', 'post']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsCommentOwner]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id', 'post']

    def perform_create(self, serializer):
        serializer.save(profile=models.Profile.objects.get(
            user=self.request.user))


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id', 'post']


class UserCreateAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class LoginView(knox.views.LoginView):
    def get_post_response_data(self, request, token, instance):
        UserSerializer = self.get_user_serializer_class()

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token,
            'user': request.user.id,
            'first_name': request.user.first_name,
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data
        return data
