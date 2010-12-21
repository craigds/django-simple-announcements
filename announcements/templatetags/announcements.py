from django.conf import settings
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag
def dismiss_js_link(a):
    ANNOUNCEMENTS_JS_NAMESPACE = getattr(settings, 'ANNOUNCEMENTS_JS_NAMESPACE', 'Announcements')
    ANNOUNCEMENTS_COOKIE_NAME = getattr(settings, 'ANNOUNCEMENTS_COOKIE_NAME', 'announcements_dismiss')
    
    return mark_safe(u"%s.dismiss('%s', '%s')" % (
        ANNOUNCEMENTS_JS_NAMESPACE,
        ANNOUNCEMENTS_COOKIE_NAME,
        a.pk
    ))

