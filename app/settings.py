# -*- coding: utf-8 -*-

import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'rvomfp)$@g8=y=1zh0uq^2&&oj-8#6e1q-v6lxjk3_)(8d4^g_'

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydb',
    }
}

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'zipcode',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '..', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

PROJECT_DIR = PROJECT_PATH

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'media')

STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'static')

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'zipcode/zipcode.log'),
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'verbose',
        },
        'null': {
            'class': 'django.utils.log.NullHandler',
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['log_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['null', ],
        },
        'zipcode': {
            'handlers': ['log_file'],
            'level': 'DEBUG',
        },
    }
}
