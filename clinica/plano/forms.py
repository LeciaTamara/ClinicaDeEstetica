from django.forms import ModelForm, fields
from django import forms
from django.db import models

from servico.models import Servico
from .models import Plano

class PlanoForm(forms.ModelForm):
    #criar o campo com mutiplas seleções
    servico = forms.ModelMultipleChoiceField(
        queryset=Servico.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'select-multiple'})
    )
    class Meta:
        model = Plano
        fields = ['tipo', 'preco', 'servico']

        widgets = {
            'tipo': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Tipo'}),

            'preco': forms.NumberInput(attrs={
                'class': 'form-control py border-white bg transparent text-black w-50', 'placeholder': 'Preco'}),
        }

class EditPlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['tipo', 'preco', 'servico']

        widgets = {
            'tipo':forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Tipo'}),
            
            'preco': forms.NumberInput(attrs={
                'class': 'form-control py border-white bg transparent text-black w-50', 'placeholder': 'Preco'}),
        }