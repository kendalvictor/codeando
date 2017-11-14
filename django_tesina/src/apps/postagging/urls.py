from django.conf.urls import url, include

from .views import cargar, listar, xml_sync
from .api.views import ExtraerAPIView, SyncAPIView

urlpatterns = [
    url(r'^corpus/',
        include([
            url(r'^sincronizar', xml_sync, name="sincronizar"),
        ])),
    url(r'^peruanismos/',
        include([
            url(r'^cargar', cargar, name="cargar"),
            url(r'^listar', listar, name="listar"),
        ])),
    url(r'^api/',
        include([
            url(r'^extraer', ExtraerAPIView.as_view(), name="extraer"),
            url(r'^sync', SyncAPIView.as_view(), name="sync"),
        ])),
]
