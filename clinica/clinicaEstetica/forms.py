from django.forms import ModelForm, fields
from django import forms
from django.db import models
from .models import Clinica
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Criar usuário 
class AdicionarUsuarioForm(UserCreationForm): 
    class Meta: 
        model = User 
        fields = ['username','email', 'password1', 'password2']

        #Adiciona estilos nos campos da senha
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Senha'})
       
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Confirme a senha'})


#Criar clínica
class ClinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = ['nome', 'sobre']

        '''estilizandp com bootstrap direto no forms.py'''
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Nome'}),

            'sobre' : forms.Textarea(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','rows' : 6, 'cols' : 50, 'placeholder': 'Fale um pouco sobre a clínica'
            })
        }

#Editar clínica
class EditClinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = ['nome', 'sobre']
        '''estilizandp com bootstrap direto no forms.py'''
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Nome'}),

            'sobre' : forms.Textarea(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','rows' : 6, 'cols' : 50, 'placeholder': 'Fale um pouco sobre a clínica'
            })
        }