# Django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
# Tastypie
from tastypie.api import Api
# Our resources
from pyday_rest.api.resources import UserResource


v1_api = Api()
v1_api.register(UserResource())

urlpatterns = patterns('',
    # URL Hook:
    url(r'^api/', include(v1_api.urls)),
)

# Admin shit
admin.autodiscover()
urlpatterns = urlpatterns + patterns('',
    # URL Hook:
    url(r'^admin/', include(admin.site.urls)),
)
