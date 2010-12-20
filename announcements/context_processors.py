from django.conf import settings
from announcements.models import Announcement

def announcements(request):
    dismissed_pk = request.session.get('announcement_dismissed', 0)
    
    qs = Announcement.objects.current().filter(pk__gt=dismissed_pk)
    qs = qs.order_by('-date_start')[:getattr(settings, 'ANNOUNCEMENTS_MAX', 1)]
    
    return {
        'announcements': qs,
    }
