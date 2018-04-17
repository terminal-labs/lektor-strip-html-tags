# -*- coding: utf-8 -*-
import re

from lektor.pluginsystem import Plugin

class StripHTMLTagsPlugin(Plugin):
    name = 'Strip HTML Tags'
    description = u'Strip HTML tags, effectively turning HTML into plain text.'

    def on_setup_env(self, **extra):
        def striphtmltags_filter(raw_html):
            '''Accept string and return with html tags removed.
            '''
            r = re.compile('<.*?>')
            rv = re.sub(r, '', str(raw_html)).strip() # Tends to have a ton of extra whitespace
            return rv
        self.env.jinja_env.filters['striphtmltags'] = striphtmltags_filter
