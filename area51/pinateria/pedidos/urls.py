from django.urls import path

from pedidos.views import Generar

urlpatterns = [
    path('generar/<int:pk>/', Generar.as_view(), name='generar'),
]
