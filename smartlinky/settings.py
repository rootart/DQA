import os

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

TEMPLATE_DEBUG = DEBUG = False
MANAGERS = ADMINS = (
    ('virtuallight', 'mat.jankowski@gmail.com'),
    ('macat', 'attila@maczak.hu')
)

# TODO: create postgreslq settings for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'sqlite3.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

SITE_ID = 1
SECRET_KEY = '&(@aujq&hv17i(_to(udw#dojx2y)yj96(&_r&x8mm75t1hsyv'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'media')
MEDIA_URL = '/site_media/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'static')
STATIC_URL = '/site_media/static/'
ADMIN_MEDIA_PREFIX = '/site_media/static/admin/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'site_media', 'media')
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = ('templates',)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'smartlinky.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.api',
    'apps.core',
    'apps.site',
    'apps.utils',
)

# TODO: format file based logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        #'file_smartlinky': {  
        #    'level': 'DEBUG',
        #    'class': 'logging.FileHandler', 
        #    'formatter': 'verbose',  
        #    'filename': os.path.join(PROJECT_ROOT, 'logs', 'smartlinky.log')
        #},

    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'smartlinky': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        }, 
    }
}

PLUGIN_FILES = (
    ('js', 'plugin', 'jquery.plugin.js'),
    ('js', 'plugin', 'jquery-ui.js'),
    ('js', 'plugin', 'style.js'),
    ('js', 'plugin', 'Button.js'),
    ('js', 'plugin', 'Widget.js'),
    ('js', 'plugin', 'Parser.js'),
    ('js', 'plugin', 'plugin.js'),
)
PLUGIN_FILENAME = 'plugin.js'
PLUGIN_CONFIG = {
    'api-url': 'http://smartlinky/api/',
}

QA_CACHE_TIMEOUT = 60 * 60
QA_LINKS_COUNT = 5
STACKOVERFLOW_VIA_GOOGLE = True

try:
    from settings_local import *
except ImportError:
    try:
        from local_settings import *
    except ImportError:
        pass
