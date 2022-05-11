from .models import *
from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm, ModelChoiceField
import datetime


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password', 'minweight', 'maxweight', 'standardweight', 'status']
#         widgets = {
#             'status': forms.RadioSelect
#         }
#         labels = {
#             "minweight": "Minimum Weight",
#             "maxweight": "Maximum Weight",
#             "standardweight": "Standard Weight",
#         }
