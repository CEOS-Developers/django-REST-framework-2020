import os
from .base import *

DATABASES['default'] = secrets['DB_SETTINGS']['default']
DEBUG = False
