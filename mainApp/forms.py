from .models import *
from django import forms
from django.forms import ModelForm
import datetime


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['id','name', 'code']

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
