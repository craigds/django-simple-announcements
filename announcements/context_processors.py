from .models import Announcement


def announcements(request):
    return {
        'announcements': Announcement.objects.for_request(request),
    }
