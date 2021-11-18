from django import forms
from django.forms import ModelForm

from django.forms import Widget
from django.forms import ModelMultipleChoiceField

from .models import Prato, Cliente, User, Pedido


class PratoForm(forms.Form):
    nome  = forms.CharField()
    descricao = forms.CharField(widget=forms.Textarea)
    valor = forms.FloatField()
    


class CadastroForm(forms.Form):

    usuario = forms.CharField()
    senha = forms.CharField()
    nome  = forms.CharField()
    cpf  = forms.CharField()
    cep  = forms.CharField()
    logradouro  = forms.CharField()
    complemento  = forms.CharField()


class PedidoForm(forms.Form):
    pedido = ModelMultipleChoiceField(queryset=Prato.objects.all(),widget=forms.CheckboxSelectMultiple)
