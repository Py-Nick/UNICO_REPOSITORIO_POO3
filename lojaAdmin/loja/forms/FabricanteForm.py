from django.forms import ModelForm
from django import forms
from loja.models.Fabricante import Fabricante

class FabricanteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None) # limpa os argumentos recorrentes do usuário
        super(FabricanteForm, self).__init__(*args, **kwargs)
        if current_user and not current_user.is_superuser:
            if self.instance and self.instance.perfil != 1:
                del self.fields['Fabricante']
    class Meta:
        model = Fabricante
        fields = ['Fabricante']
        widgets = {
            'Fabricante': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Digite o nome do fabricante'}),
        }