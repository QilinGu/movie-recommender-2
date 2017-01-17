# project wide urls
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from django.contrib import admin
admin.autodiscover()
import settings

# import your urls from each app here, as needed
import imdb.urls

urlpatterns = patterns('',

    # urls specific to this app
    url(r'^imdb/', include(imdb.urls)),

    url(r'^admin/', include(admin.site.urls)),

    # catch all, redirect to imdb home view
    #url(r'.*', RedirectView.as_view(url='/imdb/home')),
	url(r'^home/$', RedirectView.as_view(url='/imdb/home')),
	
)
