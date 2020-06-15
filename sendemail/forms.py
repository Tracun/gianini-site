from django import forms
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O telefone informado está em um formato inválido. Ex.: 11912345678")

class ContactForm(forms.Form):
    name = forms.CharField(required=True,)
    company = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, validators=[phone_regex])
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)