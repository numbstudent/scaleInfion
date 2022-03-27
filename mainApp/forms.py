from .models import *
from django import forms
from django.forms import ModelForm, ModelChoiceField
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

class ProductModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ReportBatchForm(forms.Form):
    import datetime
    productid = ProductModelChoiceField(
        queryset=Product.objects.all(), required=False, label="Product")
    batchno = forms.ModelChoiceField(queryset=Register.objects.values_list('batchno',flat=True).distinct(), required=False, label="Batch No")
    inputdatefrom = forms.DateField(required=False, label="From Date", widget=forms.DateInput(attrs={
        'class': 'form-control datetimepicker'
    }))
    inputdateto = forms.DateField(required=False, label="To Date", widget=forms.DateInput(attrs={
        'class': 'form-control datetimepicker'
    }))

