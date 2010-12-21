from announcements.models import Announcement

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import simplejson

def dismiss_announcement(request, object_id):
    # TODO Do we really need to verify the announcement exists? Could save a DB query here.
    get_object_or_404(Announcement, pk=object_id)
    
    request.session['announcements_dismissed'] = int(object_id)
    
    
    if 'next' in request.GET:
        return HttpResponseRedirect(request.GET['next'])
    else:
        # Assume AJAJ.
        # TODO: check if this is actually an ajaj request.
        # If not, should redirect to somewhere sensible (referer? /?)
        return HttpResponse('"OK"', mimetype='application/json')

def announcements_json(request):
    announcements = Announcement.objects.for_session(request.session)
    
    return HttpResponse(
        simplejson.dumps([unicode(a) for a in announcements], indent=2),
        mimetype='application/json',
    )
