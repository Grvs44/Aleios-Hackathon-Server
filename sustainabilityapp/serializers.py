from rest_framework.serializers import ModelSerializer, CharField
from . import models


class ProfileSerializer(ModelSerializer):
    class Meta:
        exclude = ['user']
        model = models.Profile


class DonationPostSerializer(ModelSerializer):
    class Meta:
        model = models.DonationPost


class EventPostSerializer(ModelSerializer):
    class Meta:
        model = models.EventPost

"""
class ImageSerializer(ModelSerializer):
    class Meta:
        model = models.Image
"""
