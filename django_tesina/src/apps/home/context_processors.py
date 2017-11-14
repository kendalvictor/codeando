# -*- coding: utf-8 -*-
from django.conf import settings


def get_menus(request):
    menus = request.session.get('menus', None)
    if menus:
        return {'menus': menus}
    return {}