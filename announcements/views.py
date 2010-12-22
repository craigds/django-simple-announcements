from announcements.models import Announcement

from django.http import HttpResponse
from django.utils import simplejson

def announcements_json(request):
    announcements = Announcement.objects.for_request(request)
    
    return HttpResponse(
        simplejson.dumps([a.to_json() for a in announcements], indent=2),
        mimetype='application/json',
    )
