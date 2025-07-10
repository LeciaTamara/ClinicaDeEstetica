from django.forms import ModelForm, fields
from django import forms
from django.db import models
from .models import Clinica

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