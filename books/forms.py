from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Libro

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password_confirm = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    show_password = forms.BooleanField(required=False, label='Mostrar contraseñas')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned = super().clean()
        pw = cleaned.get('password')
        pw2 = cleaned.get('password_confirm')
        if pw and pw2 and pw != pw2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        validate_password(pw, self.instance)
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class BookForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'estado', 'foto', 'latitud', 'longitud']
        widgets = {
            'latitud': forms.NumberInput(attrs={'step': 'any'}),
            'longitud': forms.NumberInput(attrs={'step': 'any'}),
        }
