#
# pelicanconf.py
#

# Para desarrollo
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = False

# Metadatos de todo el sitio web
SITENAME = 'CONATRIB'
SITELOGO = 'theme/images/conatrib.jpg'
SITEDESCRIPTION = '.'
SITETWITTER = '@PJCoah'

# Autor por defecto
AUTHOR = 'PJECZ'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = [
    'actividades',
]

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = [
    'conocenos',
]

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = [
    'favicon.ico',
    'LICENSE',
    'README.md',
    'robots.txt',
]

# NO usar el directorio como la categoria
USE_FOLDER_AS_CATEGORY = False

# Los artículos van en directorios por /categoria/YYYY/slug/
ARTICLE_URL = '{category}/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{slug}/index.html'

# En cada pagina debe haber metadatos url y save_as
# por lo que no necesitamos esto
# PAGE_URL = 'directorio/directorio/'
# PAGE_SAVE_AS = 'directorio/directorio/index.html'

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Monterrey'

# Para desarrollo se desactiva la generacion de feeds
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# NO BORRAR de output los siguientes directorios y archivos
OUTPUT_RETENTION = ['.git', '.gitignore']

# Paginacion
DEFAULT_PAGINATION = False
# DEFAULT_PAGINATION = True
# DEFAULT_PAGINATION = 12
# DEFAULT_ORPHANS = 2

# Para desarrollo BORRAR todo el directorio de salida
DELETE_OUTPUT_DIRECTORY = True

# Para desarrollo DESACTIVAR el caché
LOAD_CONTENT_CACHE = False

# Para desarrollo NO hay cargas desde Internet
USE_REMOTE_SERVICES = False

# Pelican plugins
# PLUGIN_PATHS = ['plugins']
# PLUGINS = []

#
# NEST Template
#
THEME = 'themes/nest'
SITESUBTITLE = 'Sitio web del CONATRIB'

# Minified CSS
NEST_CSS_MINIFY = True

# Add items to top menu before pages
MENUITEMS = [
    ('Homepage', '/'),
    ('Categories', '/categories.html'),
]

# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = ''
NEST_HEADER_LOGO = 'images/favicon.png'

# Footer
NEST_SITEMAP_COLUMN_TITLE = 'Mapa del sitio'
NEST_SITEMAP_MENU = [
    ('Archives', '/archives.html'),
    ('Tags', '/tags.html'),
    ('Authors', '/authors.html'),
]
NEST_SITEMAP_ATOM_LINK = 'Atom Feed'
NEST_SITEMAP_RSS_LINK = 'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = 'Social'
NEST_LINKS_COLUMN_TITLE = 'Links'
NEST_COPYRIGHT = '&copy; PJECZ 2020'

# Footer optional
NEST_FOOTER_HTML = ''

# index.html
NEST_INDEX_HEAD_TITLE = 'Homepage'
NEST_INDEX_HEADER_TITLE = 'My Awesome Blog'
NEST_INDEX_HEADER_SUBTITLE = 'Smashing The Stack For Fun And Profit'
NEST_INDEX_CONTENT_TITLE = 'Last Posts'

# archives.html
NEST_ARCHIVES_HEAD_TITLE = 'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = 'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = 'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = 'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = 'Archives'

# article.html
NEST_ARTICLE_HEADER_BY = 'By'
NEST_ARTICLE_HEADER_MODIFIED = 'modified'
NEST_ARTICLE_HEADER_IN = 'in category'

# author.html
NEST_AUTHOR_HEAD_TITLE = 'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = 'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = 'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = 'Posts'

# authors.html
NEST_AUTHORS_HEAD_TITLE = 'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = 'Author list'
NEST_AUTHORS_HEADER_TITLE = 'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = 'Archives listed by author'

# categories.html
NEST_CATEGORIES_HEAD_TITLE = 'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = 'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = 'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = 'Archives listed by category'

# category.html
NEST_CATEGORY_HEAD_TITLE = 'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = 'Category Archive'
NEST_CATEGORY_HEADER_TITLE = 'Category'
NEST_CATEGORY_HEADER_SUBTITLE = 'Category Archive'

# pagination.html
NEST_PAGINATION_PREVIOUS = 'Previous'
NEST_PAGINATION_NEXT = 'Next'

# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = 'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = 'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = 'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = 'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = 'Archives for'

# tag.html
NEST_TAG_HEAD_TITLE = 'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = 'Tag archives'
NEST_TAG_HEADER_TITLE = 'Tag'
NEST_TAG_HEADER_SUBTITLE = 'Tag archives'

# tags.html
NEST_TAGS_HEAD_TITLE = 'Tags'
NEST_TAGS_HEAD_DESCRIPTION = 'Tags List'
NEST_TAGS_HEADER_TITLE = 'Tags'
NEST_TAGS_HEADER_SUBTITLE = 'Tags List'
NEST_TAGS_CONTENT_TITLE = 'Tags List'
NEST_TAGS_CONTENT_LIST = 'tagged'
