import hashlib

from django.contrib.auth.models import User
from django.utils.html import urlize

from tastypie import fields
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization

from twitter.models import Tweet
from pyday_rest.api.validation import TwitterValidation

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
        validation = TwitterValidation()

    def dehydrate_tweet(self, bundle):
        return urlize(bundle.data['tweet'])

    def dehydrate(self, bundle):
        m = hashlib.md5()
        m.update(bundle.data['tweet'])
        bundle.data['hash'] = m.hexdigest()
        return bundle

    """
    def hydrate(self, bundle):
        tweet = bundle.data['tweet']
        bundle.data['tweet'] = " ".join([t for t in tweet.split(" ") if t])
        return bundle
    """
