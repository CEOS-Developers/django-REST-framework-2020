import os
from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "USER": "root",
        "NAME": "megabox",
        "PASSWORD": "aksen4011",
        "HOST": "localhost",
        "PORT": "3306"
    }
}
