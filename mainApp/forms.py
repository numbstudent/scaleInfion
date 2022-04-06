from .models import *
from django import forms
from django.forms import ModelForm, ModelChoiceField
import datetime


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'minweight', 'maxweight', 'status']
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

class ReportTitleModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class DepartmentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['id','name']

class ReportTitleForm(ModelForm):
    class Meta:
        model = ReportTitle
        fields = ['id','title','subtitle']

class ReportBatchForm(forms.Form):
    import datetime
    productid = ProductModelChoiceField(
        queryset=Product.objects.all(), required=False, label="Product")
    # batchno = forms.ModelChoiceField(queryset=Register.objects.values_list('batchno',flat=True).distinct(), required=False, label="Batch No")
    batchno = forms.CharField(required=False, label="Batch No")
    inputdatefrom = forms.DateField(required=False, label="From Date", widget=forms.DateInput(attrs={
        'class': 'form-control datepick'
    }))
    inputdateto = forms.DateField(required=False, label="To Date", widget=forms.DateInput(attrs={
        'class': 'form-control datepick'
    }))

class UploadBatchForm(forms.Form):
    productid = ProductModelChoiceField(
        queryset=Product.objects.all(), required=False, label="Product")
    batchno = forms.CharField(required=False, label="Batch No")
    file = forms.FileField()

class ReportBodyForm(ModelForm):
    # productid = ProductModelChoiceField(
    #     queryset=Product.objects.all(), required=False, label="Product")
    # batchno = forms.CharField(required=False, label="Batch No")
    # reporttitle = ReportTitleModelChoiceField(
    #     queryset=ReportTitle.objects.all(), required=False, label="Report Title")
    # department = DepartmentModelChoiceField(
    #     queryset=Department.objects.all(), required=False, label="Department")
    # reviewdate = 

    class Meta:
        model = Report
        fields = ['id','product','batchno','reporttitle','department','reviewdate','effectivedate','dnno','dnrev']
        labels = {
            "batchno": "Batch No",
            "reporttitle": "Report Title",
            "reviewdate": "Review Date",
            "effectivedate": "Effective Date",
            "dnno": "DN No",
            "dnrev": "DN Rev",
        }
        widgets = {
            "reviewdate": forms.DateInput(attrs={
                'class': 'form-control datepick'
            }),
            "effectivedate": forms.DateInput(attrs={
                'class': 'form-control datepick'
            }),
        }
