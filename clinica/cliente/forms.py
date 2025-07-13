from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from.models import Cliente
from django import forms

#Formulário de cadastro de clientes
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone']
        widgets = {
            'nome' : forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe seu nome'}),
            'endereco' : forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe seu nome'}),
            'telefone' : forms.NumberInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe seu nome'})
        }

#formulario para editar dados do Cliente
class EditClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone']
        widgets = {
            'nome' : forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe seu nome completo'}),
            'endereco' : forms.TextInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe seu endereço'}),
            'telefone' : forms.NumberInput(attrs={
                'class': 'form-control py-3 border-white bg-transparent text-white w-50','placeholder': 'Informe seu telefone'})
        }

#Formulário para alterar senha do cliente
class SenhaForm(UserChangeForm):
    password1 = forms.CharField(label=('Senha'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=('Senha de confirmação'), widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['password1', 'password2']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch',)
        return password2
    
    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.set_password(self.cleaned_data['password1'])
        if commit:
            cliente.save()
        return cliente
