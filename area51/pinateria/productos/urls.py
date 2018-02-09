from django.urls import path

from productos.views import Detalle

urlpatterns = [
    path('<int:pk>/', Detalle.as_view(), name='detalle'),
]
