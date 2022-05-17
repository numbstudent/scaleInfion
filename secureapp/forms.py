from .models import *
from django.contrib.auth.models import User, Group

from django import forms
from django.forms import ModelForm, ModelChoiceField
import datetime

class GroupModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class GroupAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Author.objects.filter(name__startswith='O')

    productid = GroupModelChoiceField(
        queryset=Group.objects.all(), label="Group", widget=forms.Select(attrs={
            'class': 'form-control select2bs4'
    }))
