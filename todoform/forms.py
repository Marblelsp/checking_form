from django import forms
from phonenumber_field.formfields import PhoneNumberField


class MyForm(forms.Form):
    email = forms.EmailField(required=False)
    phone = PhoneNumberField(required=False, region='RU')
    date = forms.DateField(input_formats=['%Y-%m-%d'], required=False)
    text = forms.CharField(required=False)
