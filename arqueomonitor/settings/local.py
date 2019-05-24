"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to socib_website/settings/local.py. It should not be checked into
your code repository.

"""
from arqueomonitor.settings.base import *   # pylint: disable=W0614,W0401

SECRET_KEY = 'mv+-j&*ihbvwif4c490e9fv9dfrek-%(_0oklse%94j&is9$mwe12'
DEBUG = True

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arqueomonitor',
        'USER': 'socib',
        'PASSWORD': '+s0c1b+',  
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS += (
    'django_extensions',
)
