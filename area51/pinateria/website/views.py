from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, UpdateView

from productos.models import Producto
from usuarios.models import PerfilUsuario
from website.forms import RegistroForm, PerfilForm

# from django.http import HttpResponse
# from django.views import View
#
# class Portada(View):
#     def get(self, request):
#         return HttpResponse('Hola Mundo!')


class Portada(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(Portada, self).get_context_data(**kwargs)
        contexto['nombre'] = 'Moisés'
        contexto['productos'] = Producto.objects.only('personaje', 'precio')
        contexto['edad'] = 16
        return contexto


class Buscar(ListView):
    template_name = 'buscar.html'
    model = Producto

    def get_queryset(self):
        termino = self.request.GET.get('termino')
        queryset = super(Buscar, self).get_queryset()
        if not termino:
            return queryset.none()
        queryset = queryset.filter(
            Q(personaje__iregex=termino) |
            Q(nombre_comercial__iregex=termino) |
            Q(descripcion__iregex=termino)
        )
        return queryset


class Registro(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('portada')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.email = form.cleaned_data['email']
        usuario.save()

        perfil = PerfilUsuario()
        perfil.usuario = usuario
        perfil.dni = form.cleaned_data['dni']
        perfil.save()

        login(self.request, usuario, 'django.contrib.auth.backends.ModelBackend')
        messages.info(self.request, 'Gracias por registrarte en nuestro sitio!')

        # return super(Registro, self).form_valid(form)
        return redirect('portada')


class Logout(LogoutView):
    next_page = reverse_lazy('portada')

    def get_next_page(self):
        messages.info(self.request, 'Gracias por usar nuestro sitio.')
        return super(Logout, self).get_next_page()


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('portada')


class Perfil(UpdateView):
    template_name = 'perfil.html'
    form_class = PerfilForm
    success_url = reverse_lazy('perfil')

    def get_object(self, queryset=None):
        return self.request.user.perfil

    def get_context_data(self, **kwargs):
        contexto = super(Perfil, self).get_context_data(**kwargs)
        contexto['pedidos'] = self.request.user.pedido_set.order_by('-fecha_emision')[:5]
        return contexto
