# calling this file announcements.py makes the namespace clash with the app :(

from announcements import defaults
from django.template import Library
from django.utils.safestring import mark_safe

register = Library('announcements')

@register.simple_tag
def dismiss_js_link(a):
    return mark_safe(u"%s.dismiss('%s', '%s')" % (
        defaults.ANNOUNCEMENTS_JS_NAMESPACE,
        defaults.ANNOUNCEMENTS_COOKIE_NAME,
        a.pk
    ))
