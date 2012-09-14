from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from twitter.models import Tweet


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ['password', 'is_staff', 'is_superuser']


class TweetResource(ModelResource):
    class Meta:
        queryset = Tweet.objects.all()
        resource_name = 'tweet'
