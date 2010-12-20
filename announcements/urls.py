from django.conf.urls.defaults import *

urlpatterns = patterns('announcements.views',
    (r'^dismiss/(?P<object_id>\d+)/$', 'dismiss_announcement'),
)
