from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm, PhoneNumberFormSet


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


def add_contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        phone_formset = PhoneNumberFormSet(request.POST, instance=Contact())
        if contact_form.is_valid() and phone_formset.is_valid():
            contact = contact_form.save()
            phone_formset.instance = contact
            phone_formset.save()
            return redirect('contact_list')
    else:
        contact_form = ContactForm()
        phone_formset = PhoneNumberFormSet(instance=Contact())

    return render(request, 'contacts/add_contact.html', {
        'contact_form': contact_form,
        'phone_formset': phone_formset,
    })
