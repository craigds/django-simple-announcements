from announcements.models import Announcement
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404

def dismiss_announcement(request, object_id):
    # TODO Do we really need to verify the announcement exists? Could save a DB query here.
    get_object_or_404(Announcement, pk=object_id)
    
    request.session['announcements_dismissed'] = int(object_id)
    
    return HttpResponseRedirect(request.GET.get('next', '/'))
