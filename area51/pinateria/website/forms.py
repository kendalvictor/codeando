from django import forms
from django.contrib.auth.forms import UserCreationForm

from usuarios.models import PerfilUsuario


class RegistroForm(UserCreationForm):
    # username = forms.CharField()
    # password = forms.CharField(
    #     widget=forms.PasswordInput
    # )

    email = forms.EmailField(
        required=True
    )

    dni = forms.CharField(
        required=True,
        max_length=8,
        min_length=8
    )

    def clean_dni(self):
        dni_limpio = self.cleaned_data['dni']

        if len(dni_limpio) < 8:
            self.add_error(
                'dni',
                'El DNI debe tener 8 dígitos.'
            )

        if not dni_limpio.isdigit():
            raise forms.ValidationError(
                'Introduzca sólo dígitos'
            )

        return dni_limpio

    # class Meta:
    #     model = User
    #     fields = ('username', 'password', 'email',)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ('ruc', 'direccion',)
