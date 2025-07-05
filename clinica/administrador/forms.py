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
            'nome': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Nome'}),
            
            'username': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50', 'placeholder': 'Usuário'}),
        }
    
    #Adiciona estilos nos campos da senha
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Senha'})
       
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Confirme a senha'})
