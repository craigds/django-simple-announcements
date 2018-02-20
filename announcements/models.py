# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals


from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from . import defaults


class AnnouncementQuerySet(models.QuerySet):
    def current(self):
        now = timezone.now()
        return self.filter(date_start__lte=now).filter(
            models.Q(date_end__gte=now) | models.Q(date_end__isnull=True)
        )

    def for_request(self, request):
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


class AnnouncementManager(models.Manager.from_queryset(AnnouncementQuerySet)):
    pass


@python_2_unicode_compatible
class Announcement(models.Model):
    message = models.CharField(max_length=255)
    url = models.URLField(null=False, blank=True, help_text="(Optional) - Link to a blog post with more information")
    date_created = models.DateTimeField(db_index=True, auto_now_add=True)
    date_start = models.DateTimeField(db_index=True, default=timezone.now)
    date_end = models.DateTimeField(db_index=True, null=True, blank=True)

    objects = AnnouncementManager()

    def is_current(self):
        now = timezone.now()
        if self.date_start < now:
            if self.date_end is None or self.date_end > now:
                return True
        return False

    # for great justice. (and admin prettiness)
    is_current.boolean = True

    def can_dismiss(self):
        return defaults.ANNOUNCEMENTS_DISMISSABLE

    def __str__(self):
        return self.message

    def to_html(self):
        from django.template import loader, Context
        t = loader.get_template("announcements/announcement.html")
        c = Context({
            'announcement': self,
        })
        return t.render(c)

    def to_json(self):
        return {
            'id': self.pk,
            'message': self.message,
            'url': self.url,
            'can_dismiss': self.can_dismiss(),
            'html': self.to_html(),
        }
