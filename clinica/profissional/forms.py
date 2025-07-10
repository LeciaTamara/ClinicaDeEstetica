from django.forms import ModelForm, fields
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm

from .models import Profissional

class ProfissionalForm(UserCreationForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'username', 'endereco', 'especializacao', 'numTelefone', 'salario']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Nome'}),

            'username': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Username'}),

            'endereco': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'endereco'}),


            'especializacao' : forms.Textarea(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','rows' : 6, 'cols' : 50, 'placeholder': 'Especialização'}),
            
            'numTelefone': forms.NumberInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Número de telefone'}),

            'salario': forms.NumberInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe salário'}),
        }
    
    #Adiciona estilos nos campos da senha
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Confirme a senha'})


'''formulário para atualizar as informações de funcionário'''
class EditProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['username', 'endereco', 'especializacao', 'numTelefone']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Username'}),

            'endereco': forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'endereco'}),

            'especializacao' : forms.Textarea(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','rows' : 6, 'cols' : 50, 'placeholder': 'Especialização'}),
            
            'numTelefone': forms.NumberInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Número de telefone'}),
        }
