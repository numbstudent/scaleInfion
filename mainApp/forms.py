from .models import *
from django import forms
from django.forms import ModelForm, ModelChoiceField
import datetime


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'minweight', 'maxweight', 'standardweight', 'status']
        widgets = {
            'status': forms.RadioSelect
        }
        labels = {
            "minweight": "Minimum Weight",
            "maxweight": "Maximum Weight",
            "standardweight": "Standard Weight",
        }

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['batchno', 'boxno']

class RejectForm(ModelForm):
    class Meta:
        model = Register
        fields = ['id']

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

class BatchnoModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.batchno

class DepartmentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class ReportTitleModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title

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

REPORTTYPE_CHOICES =(
    ("1", "Final Report"),
    ("2", "Full Report"),
)

class ReportBatchForm(forms.Form):
    import datetime
    productid = ProductModelChoiceField(
        queryset=Product.objects.all(), required=False, label="Product", widget=forms.Select(attrs={
            'class': 'form-control select2bs4'
    }))
    # batchno = forms.ModelChoiceField(queryset=Register.objects.values_list('batchno',flat=True).distinct(), required=False, label="Batch No")
    batchno = forms.CharField(required=False, label="Batch No")
    inputdatefrom = forms.DateField(required=False, label="From Date", widget=forms.DateInput(attrs={
        'class': 'form-control datepick'
    }))
    inputdateto = forms.DateField(required=False, label="To Date", widget=forms.DateInput(attrs={
        'class': 'form-control datepick'
    }))
    reporttype = forms.ChoiceField(required=False, choices=REPORTTYPE_CHOICES)

class HistoryForm(forms.Form):
    import datetime
    productid = ProductModelChoiceField(
        queryset=Product.objects.all(), required=False, label="Product", widget=forms.Select(attrs={
            'class': 'form-control select2bs4'
    }))
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
        queryset=Product.objects.all(), required=False, label="Product", widget=forms.Select(attrs={
            'class': 'form-control select2bs4'
        }))
    batchno = forms.CharField(required=False, label="Batch No")
    file = forms.FileField()


class UploadProductForm(forms.Form):
    file = forms.FileField()


class ReportBodyForm(forms.Form):
    batchno = BatchnoModelChoiceField(
        queryset=WeighingState.objects.filter(pendingstatus=False).order_by('-updatedon'), label="Batch No", widget=forms.Select(attrs={
            'class': 'form-control select2bs4'
    }))
    reporttitle = ReportTitleModelChoiceField(
        queryset=ReportTitle.objects.all(), label="Report Title", widget=forms.Select(attrs={
            'class': 'form-control select2bs4'
    }))
    department = DepartmentModelChoiceField(
        queryset=Department.objects.all(), label="Report Title", widget=forms.Select(attrs={
            'class': 'form-control select2bs4'
    }))
    reviewdate = forms.DateField(label="Review Date", widget=forms.DateInput(attrs={
        'class': 'form-control datepick'
    }))
    effectivedate = forms.DateField(label="Effective Date", widget=forms.DateInput(attrs={
        'class': 'form-control datepick'
    }))
    dnno = forms.CharField(label="DN No")
    # dnrev = forms.CharField(label="DN Rev")

# class ReportBodyForm(ModelForm):
#     # productid = ProductModelChoiceField(
#     #     queryset=Product.objects.all(), required=False, label="Product")
#     # batchno = forms.CharField(required=False, label="Batch No")
#     # reporttitle = ReportTitleModelChoiceField(
#     #     queryset=ReportTitle.objects.all(), required=False, label="Report Title")
#     # department = DepartmentModelChoiceField(
#     #     queryset=Department.objects.all(), required=False, label="Department")
#     # reviewdate = 

#     # batchno = BatchnoModelChoiceField(
#     #     queryset=WeighingState.objects.all(), required=False, label="Batch No", widget=forms.Select(attrs={
#     #         'class': 'form-control select2bs4'
#     # }))
#     class Meta:
#         model = Report
#         fields = ['id','product','batchno','reporttitle','department','reviewdate','effectivedate','dnno','dnrev']
#         labels = {
#             "batchno": "Batch No",
#             "reporttitle": "Report Title",
#             "reviewdate": "Review Date",
#             "effectivedate": "Effective Date",
#             "dnno": "DN No",
#             "dnrev": "DN Rev",
#         }
#         widgets = {
#             "reviewdate": forms.DateInput(attrs={
#                 'class': 'form-control datepick'
#             }),
#             "effectivedate": forms.DateInput(attrs={
#                 'class': 'form-control datepick'
#             }),
#         }

class WeighingStateForm(ModelForm):
    class Meta:
        model = WeighingState
        fields = ['id', 'product','batchno','status','pendingstatus']
        widgets = {
            'status': forms.RadioSelect
        }


class WeighingStateInitialForm(ModelForm):
    class Meta:
        model = WeighingState
        fields = ['id', 'product','batchno']


class WeighingStateCloseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        group = self.user.groups.all()[0].name
        super().__init__(*args, **kwargs)
        if group == 'supervisorgudang':
            self.fields['spvgudang'].required = True
            self.fields.pop("spvpabrik")
        elif group == 'supervisorproduksi':
            self.fields['spvpabrik'].required = True
            self.fields.pop("spvgudang")
        else:
            self.fields['spvgudang'].required = True
            self.fields['spvpabrik'].required = True
        # self.fields['spvpabrik'].required = True
        # self.fields['spvgudang'].required = True

    class Meta:
        model = WeighingState
        fields = ['id', 'product', 'batchno','spvpabrik','spvgudang']
        labels = {
            "spvpabrik": "Supervisor Produksi",
            "spvgudang": "Supervisor Gudang",
        }

class SimulatorForm(ModelForm):
    class Meta:
        model = Logging
        fields = ['status', 'weighing']
