from django.conf.urls.defaults import *

urlpatterns = patterns('announcements.views',
    (r'^current/$', 'announcements_json'),
    (r'^dismiss/(?P<object_id>\d+)/$', 'dismiss_announcement'),
)
