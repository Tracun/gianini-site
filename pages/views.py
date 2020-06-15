from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from sendemail.forms import ContactForm
from sendemail.views import emailContact
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index_view(request, *args, **kwargs):
    
    response = requests.post('https://d6bg74q53e.execute-api.us-east-1.amazonaws.com/dev/api/gianini/Products/scan')
    products = response.json()[0]["response"]

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
                send_mail(subject, message, "contato@gianinimanutencao.com.br", ["contato@gianinimanutencao.com.br", email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    my_content = {
        "products" : products,
        "form" : ContactForm()
    }

    return render(request, "home.html", my_content)