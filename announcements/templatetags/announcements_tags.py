# calling this file announcements.py makes the namespace clash with the app :(

from django.template import Library
from django.utils.safestring import mark_safe

from .. import defaults

register = Library()

@register.simple_tag
def dismiss_js_link(a):
    return mark_safe(u"%s.dismiss('%s', '%s')" % (
        defaults.ANNOUNCEMENTS_JS_NAMESPACE,
        defaults.ANNOUNCEMENTS_COOKIE_NAME,
        a.pk
    ))

