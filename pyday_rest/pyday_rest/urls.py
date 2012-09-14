# Django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
from pyday_rest.api import urls as api_urls
from pyday_rest.api.urls import v1_api


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
