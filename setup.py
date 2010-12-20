#!/usr/bin/env python
from distutils.core import setup

# Dynamically calculate the version based on VERSION
version_tuple = __import__('announcements').VERSION
version = ".".join([str(v) for v in version_tuple])

setup(
    name = 'django-simple-announcements',
    description = '''Basic site-wide announcements for your Django project.''',
    version = version,
    author = 'Craig de Stigter',
    author_email = 'craig.ds@gmail.com',
    url = 'http://github.com/craigds/django-simple-announcements/',
    packages=['announcements'],
    package_data={'announcements': ['templates/announcements/*']},
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
