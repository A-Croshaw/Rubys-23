from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages

def about(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_message = request.POST['contact-message']
       
        #Sending Email
        send_mail(
            contact_name,
            contact_message,
            contact_email,
            ['rubysbooksonline@gmial.com'],
        )
        messages.success(request, f'Thank you {contact_name}, We have recived your email and will be in touch soon')
        return render(request, 'about/contact.html',{'contact_name': contact_name})
    else:
        return render(request, 'about/contact.html',)