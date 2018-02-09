from django.views.generic import DetailView

from productos.models import Producto


class Detalle(DetailView):
    template_name = 'detalle.html'
    model = Producto
    context_object_name = 'producto'
