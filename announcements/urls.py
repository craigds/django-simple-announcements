from django.conf.urls.defaults import *

urlpatterns = patterns('announcements.views',
    (r'^current/$', 'announcements_json'),
)
