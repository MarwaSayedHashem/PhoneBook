from django import forms
from .models import Contact, PhoneNumber
from django.forms import inlineformset_factory

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name']

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'country_code', 'address', 'email', 'gender']

PhoneNumberFormSet = inlineformset_factory(Contact, PhoneNumber, form=PhoneNumberForm, extra=1, can_delete=True)
