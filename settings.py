#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import filters

AUTHOR = u"Lyndsy Simon"
SITENAME = u"Lyndsy Simon"
SITEURL = u'http://www.lyndsysimon.com'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'themes/mnmlist/'

DEFAULT_PAGINATION = 10
#GOOGLE_ANALYTICS = 'UA-12282897-1'
GAUGES_ID = '523cebde108d7b348d0000c9'
DISQUS_SITENAME = 'lyndsysimoncom'

JINJA_FILTERS = {
    'excerpt': filters.excerpt,
    'dt': filters.dt
}