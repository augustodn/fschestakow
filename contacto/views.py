from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import ContactForm
from farmacias.models import Pharmacy

# Create your views here.


def contact_form(request):

    pharmacy = Pharmacy.objects.get(name='schestakow')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']

            recipients = ['fschestakow@gmail.com']
            content = '%s\nCorreo: %s\nDice: %s' % (name, sender, message)
            subject = 'Correo a través de la pagina web'

            send_mail(subject,
                      content,
                      sender,
                      recipients)

            return HttpResponseRedirect('./')

    else:
        form = ContactForm()

    return render(request, 'contacto/contact.html', {'form': form,
                                                     'pharmacy': pharmacy})
