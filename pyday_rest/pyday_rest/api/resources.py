from django.contrib.auth.models import User

from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from twitter.models import Tweet


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ['password', 'is_staff', 'is_superuser']


class TweetResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Tweet.objects.all()
        resource_name = 'tweet'
        authorization = Authorization()
