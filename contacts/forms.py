from django import forms
from .models import Contact, PhoneNumber, AdditionalPhoneNumber
from django.forms import inlineformset_factory

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name']

class PhoneNumberForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('rather_not_say', 'Rather not say')
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    class Meta:
        model = PhoneNumber
        fields = ['number', 'country_code', 'address', 'email', 'gender']
        verbose_name = "Phone Number"
        verbose_name_plural = "Phone Numbers"

class AdditionalPhoneNumberForm(forms.ModelForm):
    class Meta:
        model = AdditionalPhoneNumber
        fields = ['additional_number']

PhoneNumberFormSet = inlineformset_factory(Contact, PhoneNumber,
                                           form=PhoneNumberForm, extra=1, can_delete=True)
AdditionalPhoneNumberFormSet = inlineformset_factory(Contact, AdditionalPhoneNumber,
                                                    form=AdditionalPhoneNumberForm, extra=1, can_delete=True)
