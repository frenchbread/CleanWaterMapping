from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waterproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app.views.home', name='home'),
    url(r'^new/$', 'app.views.newpoint', name='newpoint'),
    url(r'^map/$', 'app.views.mapp', name='mapp'),
    url(r'^point/(?P<point_id>\w+)/$', 'app.views.point', name='point'),
    url(r'^admin/', include(admin.site.urls)),

)
