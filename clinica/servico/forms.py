from django.forms import ModelForm, fields
from django import forms
from django.db import models
from .models import Servico, TipoServico



#Adiciona um tipo de servico
class ServicoCategoriaForm(forms.ModelForm):
    class Meta:
        model = TipoServico
        fields = ['categoria', 'imagem']

        widgets = {
            'categoria': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Categoria'}),

            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagem'].help_text = 'Adicione uma imagem'

#Editar Categoria
class EditCategoriaForm(forms.ModelForm):
    class Meta:
        model = TipoServico
        fields = ['categoria', 'imagem']

        widgets = {
            'categoria': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Categoria'}),

            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagem'].help_text = 'Adicione uma imagem'

#Adiciona Servico
class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['tipo', 'servico', 'preco', 'profissional', 'arquivo']

        widgets = {
            'servico': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Tipo'}),

            'preco': forms.NumberInput(attrs={
                'class': 'form-control py border-white bg transparent text-black w-50', 'placeholder': 'Preco'}),
            
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['arquivo'].help_text = 'Adicione uma image'

#Edite o serviço
class EditServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['tipo', 'servico', 'preco', 'profissional', 'arquivo']

        widgets = {
            'tipo':forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Categoria'}),
            
            'servico':forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Tipo'}),
            
            'preco': forms.NumberInput(attrs={
                'class': 'form-control py border-white bg transparent text-black w-50', 'placeholder': 'Preco'}),

            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['arquivo'].help_text = 'Adicione uma image'