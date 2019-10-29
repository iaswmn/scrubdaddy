import os
import re
import sys
from django.utils.translation import ugettext_lazy as _
from .pipeline import PIPELINE

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps_common'))

SECRET_KEY = 'a1^2s5%j=r9(2u7bg=*+s5t8b%3%1**qf(=rq^%#=j9dut5*8m'

DEBUG = False

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)

TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'django_cron',
    'pipeline',
    'solo',
    'suit_ckeditor',

    # Apps
    'config',
    'contacts',
    'main',
    'users',
    'products',
    'support',
    'questions',
    'where_to_buy',
    'about',
    'media',
    'std_page',
    'blog',
    'business_account',
    'employment_opportunities',
    'get_in_touch',

    # Apps common
    'admin_ctr',
    'admin_honeypot',
    'admin_log',
    'attachable_blocks',
    'backups',
    'ckeditor',
    'footer',
    'gallery',
    'breadcrumbs',
    'google_maps',
    'header',
    'menu',
    'paginator',
    'placeholder',
    'seo',
    'social_networks',
    'rating',

    # Libs
    'libs.autocomplete',
    'libs.away',
    'libs.color_field',
    'libs.file_field',
    'libs.form_helper',
    'libs.js_storage',
    'libs.management',
    'libs.pipeline',
    'libs.stdimage',
    'libs.templatetags',
    'libs.variation_field',
    'libs.sprite_image',

    # Third party apps
    'django_countries',
)

# Suit
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Scrub Daddy',

    # search
    'SEARCH_URL': '',

    # menu
    'MENU': (
        {
            'app': 'main',
            'icon': 'icon-file',
            'models': (
                'MainPageConfig',
                'MainSlider',
                'Advantage',
            )
        },
        {
            'app': 'about',
            'icon': 'icon-file',
            'models': (
                'AboutConfig',
                'Event',
            )
        },
        {
            'app': 'products',
            'icon': 'icon-file',
            'models': (
                'ProductConfig',
                'ProductCategory',
                'Product',
            )
        },
        {
            'app': 'support',
            'icon': 'icon-file',
            'models': (
                'SupportConfig',
            )
        },
        {
            'app': 'questions',
            'icon': 'icon-file',
            'models': (
                'QuestionsConfig',
                'Question',
            )
        },
        {
            'app': 'blog',
            'icon': 'icon-file',
            'models': (
                'BlogPost',
                'BlogConfig',
                'Author',
            )
        },
        {
            'app': 'media',
            'icon': 'icon-file',
            'models': (
                'MediaConfig',
                'MediaLink',
            )
        },
        {
            'app': 'where_to_buy',
            'icon': 'icon-file',
            'models': (
                'RetailConfig',
                'OnlineShopConfig',
                'InternationalConfig',
                'Country',
            )
        },
        {
            'app': 'business_account',
            'icon': 'icon-file',
            'models': (
                'BusinessAccountConfig',
                'BusinessAccountMessage',
            )
        },
        {
            'app': 'employment_opportunities',
            'icon': 'icon-file',
            'models': (
                'EmploymentOpportunitiesConfig',
                'EmploymentOpportunitiesMessage',
            )
        },
        {
            'app': 'contacts',
            'icon': 'icon-file',
            'models': (
                'Address',
                'ContactsConfig',
                'Message',
            )
        },
        {
            'app': 'get_in_touch',
            'icon': 'icon-file',
            'models': (
                'GetInTouchMessage',
                'GetInTouchConfig',
            )
        },
        '-',
        {
            'app': 'config',
            'icon': 'icon-lock',
            'models': (
                'Config',
            )
        },
        {
            'app': 'social_networks',
            'icon': 'icon-lock',
            'models': (
                # 'FeedPost',
                'SocialLinks',
                'SocialConfig',
            )
        },
        '-',
        {
            'icon': 'icon-lock',
            'label': 'Authentication and Authorization',
            'permissions': 'users.change_customuser',
            'models': (
                'auth.Group',
                'users.CustomUser',
            )
        },
        {
            'app': 'backups',
            'icon': 'icon-hdd',
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'django_cron',
            'icon': 'icon-hdd',
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'admin',
            'icon': 'icon-list-alt',
            'label': _('History'),
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'sites',
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'seo',
            'icon': 'icon-tasks',
            'permissions': 'users.admin_menu',
            'models': (
                'SeoConfig',
                'Redirect',
                'Counter',
                'Robots',
            ),
        },
    ),
}


# Pipeline
SASS_INCLUDE_DIR = BASE_DIR + '/static/scss/'
PIPELINE['SASS_BINARY'] = '/usr/bin/env sassc --load-path ' + SASS_INCLUDE_DIR

MIDDLEWARE_CLASSES = (
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'libs.geoip2.middleware.GeoIP2Middleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'libs.cache.middleware.SCCMiddleware',
    'libs.js_storage.middleware.JSStorageMiddleware',
    'libs.middleware.xss.XSSProtectionMiddleware',
    'libs.middleware.utm.UTMMiddleware',
    'menu.middleware.MenuMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    'seo.middleware.RedirectMiddleware',
)

ALLOWED_HOSTS = ()

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Sites and users
SITE_ID = 1
ANONYMOUS_USER_ID = -1
AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'index'
LOGIN_REDIRECT_URL = 'index'
RESET_PASSWORD_REDIRECT_URL = 'index'
LOGOUT_URL = 'index'

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@directlinedev.com'
EMAIL_HOST_PASSWORD = 'g83d38QWI7yZ'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'noreply@directlinedev.com'
EMAIL_SUBJECT_PREFIX = '[%s] ' % (SUIT_CONFIG['ADMIN_NAME'], )

# ==================================================================
# ==================== APPS SETTINGS ===============================
# ==================================================================

# Admin Dump
BACKUP_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'backup'))

# Директория для robots.txt и других открытых файлов
PUBLIC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'public'))

# Django solo caching
SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = 10 * 60

# Smart Cache-Control
SCC_IGNORE_URLS = [
    r'/admin/',
    r'/dladmin/',
]

# Формат валют (RUB / USD / EUR / GBP)
# Для включения зависимости от языка сайта - задать None или удалить
VALUTE_FORMAT = None

# Django Cron
CRON_CLASSES = [

]

# ==================================================================
# ==================== END APPS SETTINGS ===========================
# ==================================================================

# Домен для куки сессий (".example.com")
SESSION_COOKIE_DOMAIN = None
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 30 * 24 * 3600

# Домен для куки CSRF (".example.com")
CSRF_COOKIE_DOMAIN = None

# Список скомпилированных регулярных выражений
# запретных юзер-агентов
DISALLOWED_USER_AGENTS = ()

# Получатели писем о ошибках при DEBUG = False
ADMINS = (
    ('pix', 'x896321475@gmail.com'),
    ('kp', 'kpXXX@ya.ru'),
)

# Получатели писем о битых ссылках при DEBUG=False
# Требуется подключить django.middleware.common.BrokenLinkEmailsMiddleware
MANAGERS = (
    ('pix', 'x896321475@gmail.com'),
)

# Список скомпилированных регулярных выражений адресов страниц,
# сообщения о 404 на которых не должны отправляться на почту (MANAGERS)
IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

# DB
DATABASES = {}

# Cache
CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:0",
        "KEY_PREFIX": LANGUAGE_CODE + SECRET_KEY,
        "OPTIONS": {
            "CLIENT_CLASS": 'django_redis.client.DefaultClient',
            "PASSWORD": "",
        }
    }
}

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            'templates',
            os.path.join(BASE_DIR, 'templates'),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'social_networks.context_processors.google_apikey',
                'libs.context_processors.domain',
            ),
        }
    },
]

# Locale
LOCALE_PATHS = (
    'locale',
)

# Datetime formats
FORMAT_MODULE_PATH = [
    'project.formats',
]

# Media
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'media'))
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
