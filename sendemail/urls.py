from django.contrib import admin
from django.urls import path

from .views import emailContact, successView

urlpatterns = [
    path('contact/', emailContact, name='contact'),
    path('success/', successView, name='success'),
]