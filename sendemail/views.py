from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailContact(request, *args, **kwargs):
    if request.method == 'GET':
        form = ContactForm()
    else:
        print("SEND EMAIL")
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'] 
            company = form.cleaned_data['company']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, "contato@gianinimanutencao.com.br", [email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "home.html", args[0])

def successView(request):
    return render(request, "msgEnviada.html", {})