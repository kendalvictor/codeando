from django.contrib import admin

from pedidos.models import Pedido


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'estado', 'producto', 'cantidad', 'fecha_emision',)
    list_display_links = list_display
    list_filter = ('estado', 'fecha_emision',)


admin.site.register(Pedido, PedidoAdmin)
