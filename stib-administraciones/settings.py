# Django settings for riauditoria.
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.dirname(__file__)


# DEBUG
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Buenos_Aires'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-es'

SITE_ID = 5

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static_ files should be collected to.
# Don't put anything in this directory yourself; store your static_ files
# in apps' "static_/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static_/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static_ files.
# Example: "http://media.lawrence.com/static_/"
STATIC_URL = '/static/'

# Additional locations of static_ files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'staticfiles'),
)

# List of finder classes that know how to find static_ files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e89^m%8%qx)qfj^m8@*=pp9wyg=sujhy*z9xty4f^x)tzq7_&amp;m'

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
)
# END MIDDLEWARE CONFIGURATION


# TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    #'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    # Your stuff: custom template context processers go here
    'stib-administraciones.edificios.context_processors.edificios_usuarios',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'
# END TEMPLATE CONFIGURATION

ROOT_URLCONF = 'stib-administraciones.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'stib-administraciones.wsgi.application'

# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'south',
    'easy_thumbnails',
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'imperavi',
    'taggit',
    'pagination',
    'disqus',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'stib-administraciones.users',  # custom users app
    'stib-administraciones.perfiles', # perfiles de usuarios
    'stib-administraciones.edificios', # perfiles de edificios
    'stib-administraciones.llaves', # llaves de edificios
    'stib-administraciones.personales', # personales que trabajan en un edificio
    'stib-administraciones.horarios', # horarios de los edificios
    'stib-administraciones.contactos', # contactos de los edificios
    'stib-administraciones.fotos', # fotos de los edificios
    'stib-administraciones.productos', # productos
    'stib-administraciones.servicios', # servicios
    'stib-administraciones.relaciones', # relaciones
    'stib-administraciones.flatpagesx', # flatpagesx
    'stib-administraciones.feedbacks', # feedbacks
    'stib-administraciones.novedades', # novedades
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'
# END Custom user app defaults

# Thumbnail images
THUMBNAIL_ALIASES = {
    '': {
        '70x70': dict(size=(70, 70), quality=75, crop="center"),
        'small': dict(size=(50, 50), quality=75, crop="center"),
    }
}
# end Thumbnail images

# Disqus
DISQUS_API_KEY = 'uqHEQ4RlBF6Vb6Lq4pUXXV5zusjm4wc5pZwbIyV324cbJ5ZZbAnUZZadG8ShKFt3'
DISQUS_WEBSITE_SHORTNAME = 'StibAdministraciones'
# / Disqus


# --------------------------
#  IMPORT LOCAL SETTINGS
# --------------------------
try:
    from settings_local import *
except ImportError:
    pass
