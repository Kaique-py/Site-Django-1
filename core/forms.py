from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Cadastro(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') #Senha 1 e senha 2 são apenas para o usuário repetir e vermos se ele escrever a senha igual, na hora de se cadastrar.

        #Aqui vamos deixar um pouco mais arrumadinho cada um dos campos:
        username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Seu nome de usuário',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
        email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'Seu endereço de e-mail',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Senha',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita sua senha',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
        #Percebam, in loco, que não mudou nada no site...