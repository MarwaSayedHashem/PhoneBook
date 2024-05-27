from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, PhoneNumber, AdditionalPhoneNumber
from .forms import ContactForm, PhoneNumberFormSet, AdditionalPhoneNumberFormSet

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})



def add_contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        phone_formset = PhoneNumberFormSet(request.POST, prefix='phones')
        additional_phone_formset = AdditionalPhoneNumberFormSet(request.POST, prefix='additional_phones')

        # Step 1: Check form validity
        if contact_form.is_valid() and phone_formset.is_valid() and additional_phone_formset.is_valid():
            # Step 2: Verify formset association
            contact = contact_form.save()
            phone_formset.instance = contact
            phone_formset.save()

            additional_phone_formset.instance = contact
            additional_phone_formset.save()

            return redirect('contact_list')
        else:
            # Step 3: Check for validation errors
            print("Contact Form Errors:", contact_form.errors)
            print("Phone Formset Errors:", phone_formset.errors)
            print("Additional Phone Formset Errors:", additional_phone_formset.errors)
            # Additional debugging steps can be added here as needed

    else:
        contact_form = ContactForm()
        phone_formset = PhoneNumberFormSet(prefix='phones')
        additional_phone_formset = AdditionalPhoneNumberFormSet(prefix='additional_phones')

    return render(request, 'contacts/add_contact.html', {
        'contact_form': contact_form,
        'phone_formset': phone_formset,
        'additional_phone_formset': additional_phone_formset,
    })
