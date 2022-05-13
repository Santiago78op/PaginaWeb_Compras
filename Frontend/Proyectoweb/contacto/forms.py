import email
from urllib import request
from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label="contenido", widget=forms.Textarea)
    