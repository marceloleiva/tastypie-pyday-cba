from tastypie.api import Api
from pyday_rest.api.resources import UserResource, TweetResource


v1_api = Api()
v1_api.register(UserResource())
v1_api.register(TweetResource())
