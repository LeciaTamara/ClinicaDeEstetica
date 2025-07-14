from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm
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

#formulario para editar dados do Administrador
class EditAdmForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nome']
        widgets = {
            'nome' : forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe seu nome completo'}),
        }

#Formulário para alterar senha do administrador
class SenhaForm(UserChangeForm):
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Senha de confirmação',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Administrador
        fields = ['password1', 'password2']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch',)
        return password2
    
    def save(self, commit=True):
        administrador = super().save(commit=False)
        administrador.user.set_password(self.cleaned_data['password1'])
        administrador.user.save()
        if commit:
            administrador.save()
        return administrador