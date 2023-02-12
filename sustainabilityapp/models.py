from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.forms import ValidationError


category_choices = IntegerChoices('Category', 'Food Item Event')

class User(AbstractUser):
    bio = CharField(max_length=100)
    join_date = DateField(auto_now_add=True)
    interested = ManyToManyField('Post', related_name='interested', blank=True)
    score = PositiveIntegerField(default=0, blank=False, null=False)


class Tag(Model):
    category = PositiveSmallIntegerField(choices=category_choices.choices)
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(Model):
    owner = ForeignKey(User, on_delete=CASCADE)
    category = PositiveSmallIntegerField(choices=category_choices.choices)
    description = TextField()
    post_time = DateTimeField(auto_now_add=True)
    modified_time = DateTimeField(auto_now=True)
    start_time = DateTimeField(blank=True, null=True)
    end_time = DateTimeField(blank=True, null=True)
    tags = ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return '%s by %s at %s' % (str(self.category), str(self.owner), str(self.post_time))


class Comment(Model):
    post = ForeignKey(Post, on_delete=CASCADE)
    owner = ForeignKey(User, on_delete=CASCADE)
    text = TextField()
    post_time = DateTimeField(auto_now_add=True)


class Image(Model):
    post = ForeignKey(Post, on_delete=CASCADE)
    alt_text = CharField(max_length=50)
    image = ImageField()

    def __str__(self):
        return 'Image "%s" for post %s' % (str(self.alt_text), str(self.post))
