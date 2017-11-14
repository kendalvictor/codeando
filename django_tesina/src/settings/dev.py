# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

THIRD_PART_APPS += [
    'django_extensions',
    #'debug_toolbar',
    'rest_framework'
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': True,
}


