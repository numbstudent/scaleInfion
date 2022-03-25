from .models import *
from django import forms
from django.forms import ModelForm
import datetime


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['id','name', 'code', 'status']
        widgets = {
            'status': forms.RadioSelect
        }

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['batchno', 'boxno', 'status']

class LoggingForm(ModelForm):
    class Meta:
        model = Logging
        fields = ['weighing']

class PrintHeaderForm(ModelForm):
    class Meta:
        model = PrintHeader
        fields = ['name', 'label', 'imageurl']
