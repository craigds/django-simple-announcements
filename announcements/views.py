from announcements.models import Announcement

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import simplejson

def announcements_json(request):
    announcements = Announcement.objects.for_request(request)
    
    return HttpResponse(
        simplejson.dumps([unicode(a) for a in announcements], indent=2),
        mimetype='application/json',
    )
