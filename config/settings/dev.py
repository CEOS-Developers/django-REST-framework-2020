import os
from .base import *

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
