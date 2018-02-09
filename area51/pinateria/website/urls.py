from django.urls import path

from website.views import Portada, Buscar, Registro, Logout, Login, Perfil

urlpatterns = [
    path('buscador/', Buscar.as_view(), name='buscar'),
    path('registro/', Registro.as_view(), name='registro'),

    path('logout/', Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name='login'),

    path('perfil/', Perfil.as_view(), name='perfil'),

    path('', Portada.as_view(), name='portada')
]
