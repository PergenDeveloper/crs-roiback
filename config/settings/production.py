import os
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

STRING_ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")

if STRING_ALLOWED_HOSTS:
    ALLOWED_HOSTS = STRING_ALLOWED_HOSTS.split(',')
