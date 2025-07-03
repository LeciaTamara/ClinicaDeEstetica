from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from .models import Administrador

'''Formulário para adicionar Administrador'''
class AdministradorForm(UserCreationForm):
    class Meta:
        model = Administrador
        fields = ['nome', 'username']
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'nome'})
        }