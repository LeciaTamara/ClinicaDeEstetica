from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from .models import Administrador

#Formulário para adicionar Administrador
class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe seu nome'}),
            
        }