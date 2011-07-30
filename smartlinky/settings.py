import os
import sys

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))


TEMPLATE_DEBUG = DEBUG = False
MANAGERS = ADMINS = (
    ('virtuallight', 'mat.jankowski@gmail.com'),
    ('macat', 'attila@maczak.hu')
)

# TODO: create postgreslq settings for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

SITE_ID = 1
SECRET_KEY = '&(@aujq&hv17i(_to(udw#dojx2y)yj96(&_r&x8mm75t1hsyv'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = 'media'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = ()
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
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.utils',
    'apps.core',
    'apps.api',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

PLUGIN_FILES = (
    ('js', 'plugin', 'jquery.plugin.js'),
    ('js', 'plugin', 'Parser.js'),
    ('js', 'plugin', 'plugin.js'),
)
PLUGIN_FILENAME = 'plugin.js'
PLUGIN_CONFIG = {
    'api-url': 'http://smartlinky/api/',
}

try:
    from settings_local import *
except:
    pass
