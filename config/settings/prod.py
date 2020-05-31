import os
from .base import *

ALLOWED_HOSTS = secrets['ALLOWED_HOST']

DATABASES['default'] = secrets['DB_SETTINGS']['default']
DEBUG = False


