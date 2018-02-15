# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

THIRD_PART_APPS += [
    'django_extensions'
]

LOCAL_APPS += [
    'apps.postagging'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS
