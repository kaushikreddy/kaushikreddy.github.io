#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kaushik'
SITENAME = "Kaushik's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/kaushikreddy/'),
          ('Github', 'https://github.com/kaushikreddy/'),)

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU = False

TAG_CLOUD_STEPS = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/pelican-bootstrap3"


#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME ="yeti"
PLUGIN_PATHS = ['plugins']
#PLUGINS = ['assets', 'sitemap', 'gravatar']

PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'i18n_subsites','assets', 'sitemap', 'gravatar','assets','tag_cloud'
           ]

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
