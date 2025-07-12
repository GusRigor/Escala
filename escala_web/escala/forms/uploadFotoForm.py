from django import forms

class UploadFotoForm(forms.Form):
    imagem = forms.ImageField()