from .models import *
from django.contrib.auth.models import User, Group

from django import forms
from django.forms import ModelForm, ModelChoiceField 
from django.contrib.auth.forms import UserCreationForm

import datetime

class GroupModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class GroupAddForm(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.queryset = Group.objects.filter(name__startswith='O')

    group = GroupModelChoiceField(
        queryset=Group.objects.all(), label="Group", widget=forms.Select(attrs={
            'class': 'form-control select2bs4'
    }))

class FeatureAccessForm(ModelForm):
    class Meta:
        model = AccessList
        fields = ['feature_name', 'allowed_groups']
        widgets = {
            "feature_name": forms.DateInput(attrs={
                'readonly': True
            }),
            "allowed_groups": forms.CheckboxSelectMultiple(),
            
        }

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'password1' ,'password2' )