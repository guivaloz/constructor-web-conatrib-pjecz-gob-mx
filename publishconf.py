#
# publishconf.py
#

from pelicanconf import *

# Para producción los URLs son absolutos
SITEURL = 'https://conatrib.pjecz.gob.mx'
SITELOGO = 'https://conatrib.pjecz.gob.mx/theme/images/conatrib.jpg'
RELATIVE_URLS = False

# Para producción se activa la generacion de feeds
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
FEED_MAX_ITEMS = 24
RSS_FEED_SUMMARY_ONLY = True

# Paginacion
# DEFAULT_PAGINATION = False
DEFAULT_PAGINATION = True
DEFAULT_PAGINATION = 12
DEFAULT_ORPHANS = 2

# Pelican plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 1,
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
    'exclude': [
        'archives.html',
        'tags.html',
        'categories.html',
        'author/',
    ],
}

# Para producción NO BORRAR todo el directorio de salida
DELETE_OUTPUT_DIRECTORY = False

# Para producción activar el caché
LOAD_CONTENT_CACHE = True

# Para producción SI hay cargas desde Internet
USE_REMOTE_SERVICES = True
