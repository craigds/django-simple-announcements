from django.contrib import admin

from .models import Announcement

class AnnouncementOptions(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'date_start', 'date_end', 'is_current', 'message',)
    list_display_links = ('id', 'date_created', 'date_start', 'date_end',)

admin.site.register(Announcement, AnnouncementOptions)
