from django.urls import reverse_lazy
from django.views.generic import FormView

from pedidos.forms import PedidoForm
from productos.models import Producto


class Generar(FormView):
    template_name = 'generar.html'
    form_class = PedidoForm
    success_url = reverse_lazy('portada')

    def get_context_data(self, **kwargs):
        contexto = super(Generar, self).get_context_data(**kwargs)
        contexto['producto'] = self.get_producto()
        return contexto

    def form_valid(self, form):
        pedido = form.save(commit=False)
        pedido.producto = self.get_producto()
        pedido.usuario = self.request.user
        pedido.save()
        return super(Generar, self).form_valid(form)

    def get_producto(self):
        return Producto.objects.get(id=self.kwargs['pk'])
