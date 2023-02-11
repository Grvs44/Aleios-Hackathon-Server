from django.db.models import *
from django.conf import settings


class Profile(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    user_name = CharField(max_length=50, blank=False)
    bio = CharField(max_length=100)
    join_date = DateField(auto_now_add=True)


class Post(Model):
    owner = ForeignKey(Profile, on_delete=CASCADE)
    description = TextField()
    #interested = ManyToManyField(Profile, related_name='profile_interested')
    post_time = DateTimeField(auto_now_add=True)
    modified_time = DateTimeField(auto_now=True)
    image_alt_text = CharField(max_length=50)
    image = ImageField(upload_to='uploads/')

    class Meta:
        abstract = True


class DonationPost(Post):
    pass


class EventPost(Post):
    start_time = DateTimeField()
    end_time = DateTimeField()

"""
class Image(Model):
    post = ForeignKey(Post, on_delete=CASCADE)
    alt_text = CharField(max_length=50)
    image = ImageField(upload_to='uploads/')
"""
