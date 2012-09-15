from django.contrib.auth.models import User

from tastypie import fields
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization

from twitter.models import Tweet


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ['password', 'is_staff', 'is_superuser']

        filtering = {
            'username': ALL,
            'date_joined': ['range', 'gt', 'gte', 'lt', 'lte'],
        }


class TweetResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Tweet.objects.all()
        resource_name = 'tweet'
        authorization = Authorization()
