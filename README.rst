
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

2. Copy or symlink ``media/js/announcements.js`` into your ``MEDIA_ROOT``.

3. Do a db sync::
    
    python manage.py syncdb

4. Start announcing things at /admin/announcements/announcement/
