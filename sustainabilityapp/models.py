from django.db.models import *
from django.conf import settings


class Profile(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    bio = CharField(max_length=100)
    join_date = DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Post(Model):
    owner = ForeignKey(Profile, on_delete=CASCADE)
    description = TextField()
    interested = ManyToManyField(Profile, related_name='interested')
    post_time = DateTimeField(auto_now_add=True)
    modified_time = DateTimeField(auto_now=True)
    start_time = DateTimeField()
    end_time = DateTimeField()

    def __str__(self):
        return '%s at %s' % (str(self.owner), str(self.post_time))


class Image(Model):
    post = ForeignKey(Post, on_delete=CASCADE)
    alt_text = CharField(max_length=50)
    image = ImageField(upload_to='uploads/')

    def __str__(self):
        return 'Image "%s" for post %s' % (str(self.alt_text), str(self.post))
