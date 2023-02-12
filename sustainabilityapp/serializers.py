from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model
from . import models


class PostSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Post


class ImageSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Image


class CommentSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Comment


class TagSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = models.Tag


# https://stackoverflow.com/questions/43031323/how-to-create-a-new-user-with-django-rest-framework-and-custom-user-model
class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name',
                  'username', 'password', 'interested')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
