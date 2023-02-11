from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import User
from . import models


class ProfileSerializer(ModelSerializer):
    class Meta:
        exclude = ['user']
        model = models.Profile


class PostSerializer(ModelSerializer):
    class Meta:
        model = models.Post


class ImageSerializer(ModelSerializer):
    class Meta:
        model = models.Image


# https://stackoverflow.com/questions/43031323/how-to-create-a-new-user-with-django-rest-framework-and-custom-user-model
class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
