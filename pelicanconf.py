#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Swati S M'
SITENAME = 'Swadss Blog'
SITEURL = ''
OUTPUT_PATH='blog/output'
PLUGIN_PATHS=['plugins/i18n_subsites/',]
PLUGINS=['i18n_subsites',]
JINJA_ENVIRONMENT = {
'extensions': ['jinja2.ext.i18n']
}
BOOTSTRAP_THEME='flatly'
PYGMENTS_STYLE='monokai'
PATH = 'content'
THEME='pelican-themes/pelican-bootstrap3'
TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Swati76813533'),
          ('linkedIn', 'https://www.linkedin.com/in/swati-s-maddur-6b4386182'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
