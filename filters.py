import re
import datetime


def excerpt(content):
    return re.split(r'<h[1-6][^>]*>',content)[0]


dt = lambda x: x.strftime('%b %d, %Y')