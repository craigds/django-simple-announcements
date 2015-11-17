
===========================
django-simple-announcements
===========================

A simpler alternative to django-announcements.


Features
--------

 * Site-wide announcements
 * Create announcements in the admin interface
 * Start and end dates for announcements
 * Per-session dismiss links


Getting started
---------------

1. Add 'announcements' to your ``settings.INSTALLED_APPS``.

2. Add 'announcements.context_processors.announcements' to your ``settings.TEMPLATE_CONTEXT_PROCESSORS``.

3. Copy or symlink ``media/js/announcements.js`` into your ``MEDIA_ROOT``.

4. Migrate::
    
    django-admin migrate

5. Include ``announcements/announcements.html`` somewhere, probably in your ``base`` template::

    {% include "announcements/announcements.html" %}

6. Start announcing at ``/admin/announcements/announcement/``

Requirements:
-------------

 * Python 2.7 or 3.3+
 * Django 1.7+
