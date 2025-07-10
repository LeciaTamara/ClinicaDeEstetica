from django.forms import ModelForm, fields
from django import forms
from django.db import models
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['tipo', 'preco', 'profissional']

        widgets = {
            'tipo': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Tipo'}),

            'preco': forms.NumberInput(attrs={
                'class': 'form-control py border-white bg transparent text-black w-50', 'placeholder': 'Preco'}),
        }

class EditServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['tipo', 'preco', 'profissional']

        widgets = {
            'tipo':forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Tipo'}),
            
            'preco': forms.NumberInput(attrs={
                'class': 'form-control py border-white bg transparent text-black w-50', 'placeholder': 'Preco'}),
        }