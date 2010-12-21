
from datetime import datetime
from django.conf import settings
from django.db import models

class AnnouncementManager(models.Manager):
    def current(self):
        now = datetime.now()
        return self.get_query_set().filter(date_start__lte=now).filter(
            models.Q(date_end__gte=now) | models.Q(date_end__isnull=True)
        )

class Announcement(models.Model):
    message = models.CharField(max_length=255)
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
    
    def can_dismiss(self):
        return getattr(settings, "ANNOUNCEMENTS_DISMISSABLE", True)
    
    def __unicode__(self):
        return unicode(self.message)
