from django.db import models
from django.core.mail import send_mail

# Create your models here.
def send_email(form):
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
