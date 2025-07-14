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
                'class': 'form-control py-3 border-white bg transparent text-black w-100 mb-3 mt-4', 'placeholder': 'Categoria'}),

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
        fields = ['tipo', 'servico', 'preco', 'profissional', 'descricao', 'arquivo']

        widgets = {
            'servico': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg transparent text-black w-50', 'placeholder': 'Tipo'}),

            'preco': forms.NumberInput(attrs={
                'class': 'form-control py border-white bg transparent text-black w-50', 'placeholder': 'Preco'}),

            'descricao' : forms.Textarea(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','rows' : 6, 'cols' : 50, 'placeholder': 'Especialização'}),
            
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['arquivo'].help_text = 'Adicione uma image'

#Edite o serviço
class EditServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['tipo', 'servico', 'preco', 'profissional', 'descricao', 'arquivo']

        widgets = {
            'servico': forms.TextInput(attrs={
                'class': 'form-control w-100 mb-3', 'rows': 6,
                'placeholder': 'Tipo'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control w-100 mb-3',
                'placeholder': 'Preço'
            }),
            'profissional': forms.Select(attrs={
                'class': 'form-control w-100 mb-3'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control w-100 mb-3',
                'rows': 6,
                'placeholder': 'Especialização'
            }),
            'arquivo': forms.ClearableFileInput(attrs={
                'class': 'form-control w-100 mb-3'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['arquivo'].help_text = 'Adicione uma imagem'