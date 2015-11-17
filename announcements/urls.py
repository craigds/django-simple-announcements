from django.conf.urls import url
from .views import announcements_json

urlpatterns = [
    url(r'^current/$', announcements_json),
]
