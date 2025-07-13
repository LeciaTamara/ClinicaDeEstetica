from django.contrib.auth.forms import UserCreationForm


from.models import Cliente
from django import forms
#Formulário de cadastro de clientes
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone']
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'informe o seu nome'}),
            'endereco' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'informe o seu endereço'}),
            'telefone' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'informe o seu número de telefone' })
        }