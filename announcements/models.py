
from datetime import datetime
from django.db import models

class AnnouncementManager(models.Manager):
    def current(self):
        now = datetime.now()
        return self.get_query_set().filter(date_start__lte=now).filter(
            models.Q(date_end__gte=now) | models.Q(date_end__isnull=True)
        )
    
    def for_request(self, request):
        from announcements import defaults
        cookie_name = defaults.ANNOUNCEMENTS_COOKIE_NAME
        cookie = request.COOKIES.get(cookie_name, None)
        
        dismissed_pk = 0
        if cookie:
            try:
                dismissed_pk = int(cookie)
            except ValueError:
                pass
        
        qs = self.current().filter(pk__gt=dismissed_pk)
        qs = qs.order_by('-date_start')[:defaults.ANNOUNCEMENTS_MAX]
        return qs

class Announcement(models.Model):
    message = models.CharField(max_length=255)
    # verify_exists=False until this bugfix lands in Django: http://code.djangoproject.com/ticket/9857
    url = models.URLField(null=False, blank=True, verify_exists=False, help_text="(Optional) - Link to a blog post with more information")
    date_created = models.DateTimeField(db_index=True, auto_now_add=True)
    date_start = models.DateTimeField(db_index=True)
    date_end = models.DateTimeField(db_index=True, null=True, blank=True)
    
    objects = AnnouncementManager()

    def is_current(self):
        now = datetime.now()
        if self.date_start < now:
            if self.date_end is None or self.date_end > now:
                return True
        return False
    
    # for great justice. (and admin prettiness)
    is_current.boolean = True
    
    def can_dismiss(self):
        from announcements import defaults
        return defaults.ANNOUNCEMENTS_DISMISSABLE
    
    def __unicode__(self):
        return unicode(self.message)
    
    def to_json(self):
        return {
            'id': self.pk,
            'message': self.message,
            'url': self.url,
            'can_dismiss': self.can_dismiss(),
        }
