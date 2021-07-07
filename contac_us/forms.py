from django import forms
from django.db.models import fields
from django.utils import version
from django.forms import ModelForm
from .models import ConatacUS

class ContactForm(ModelForm):
    class Meta:
        model = ConatacUS
        fields = '__all__'