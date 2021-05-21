import os
from .base import *  # noqa

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
STRING_ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
if STRING_ALLOWED_HOSTS:
    ALLOWED_HOSTS = STRING_ALLOWED_HOSTS.split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('SQLITE3_FILEPATH'),
    }
}

# SECURITY
# ------------------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = os.environ.get('DJANGO_SECURE_SSL_REDIRECT', default='True') == 'True'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get(
    'DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default='True'
) == 'True'
SECURE_HSTS_PRELOAD = os.environ.get('DJANGO_SECURE_HSTS_PRELOAD', default='True') == 'True'
SECURE_CONTENT_TYPE_NOSNIFF = os.environ.get(
    'DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default='True'
) == 'True'
