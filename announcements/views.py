import json

from django.http import HttpResponse

from .models import Announcement

def announcements_json(request):
    announcements = Announcement.objects.for_request(request)

    return HttpResponse(
        json.dumps([a.to_json() for a in announcements], indent=2),
        content_type='application/json',
    )
