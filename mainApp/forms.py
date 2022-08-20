from .models import *
from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

class MultiWidgetBasic(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.Select(choices=MONTH_CHOICES, attrs={'class': 'form-control select2bs4  col-lg-2'}),
                   forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-control select2bs4  col-lg-2'})]
        super(MultiWidgetBasic, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        else:
            return ['', '']


class MultiExampleField(forms.fields.MultiValueField):
    widget = MultiWidgetBasic

    def __init__(self, *args, **kwargs):
        list_fields = [forms.fields.ChoiceField(choices=MONTH_CHOICES),
                       forms.fields.ChoiceField(choices=YEAR_CHOICES)]
        super(MultiExampleField, self).__init__(list_fields, *args, **kwargs)

    def compress(self, values):
        ## compress list to single object                                               
        ## eg. date() >> u'31/12/2012'                                                  
        # return pickle.dumps(values)
        return values[0]+' '+values[1]

class ProductForm(ModelForm):
    class Meta:
        model = Product
        # fields = ['id', 'name', 'code', 'minweight', 'maxweight', 'standardweight', 'status']
        fields = ['id', 'name', 'code', 'minweight', 'maxweight', 'standardweight', 'jumlahkoli']
        # widgets = {
        #     'status': forms.RadioSelect
        # }
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
    ("1", "OK / LAST BOX ONLY"),
    ("2", "AUDIT TRAIL"),
)
MONTH_CHOICES =(
    ('JAN', 'JAN'),
    ('FEB', 'FEB'),
    ('MAR', 'MAR'),
    ('APR', 'APR'),
    ('MAY', 'MAY'),
    ('JUN', 'JUN'),
    ('JUL', 'JUL'),
    ('AUG', 'AUG'),
    ('SEP', 'SEP'),
    ('OCT', 'OCT'),
    ('NOV', 'NOV'),
    ('DEC', 'DEC'),
)
YEAR_CHOICES =(
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
    ("25", "25"),
    ("26", "26"),
    ("27", "27"),
    ("28", "28"),
    ("29", "29"),
    ("30", "30"),
    ("31", "31"),
    ("32", "32"),
    ("33", "33"),
    ("34", "34"),
    ("35", "35"),
    ("36", "36"),
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40"),
    ("41", "41"),
    ("42", "42"),
    ("43", "43"),
    ("44", "44"),
    ("45", "45"),
    ("46", "46"),
    ("47", "47"),
    ("48", "48"),
    ("49", "49"),
    ("50", "50"),
    ("51", "51"),
    ("52", "52"),
    ("53", "53"),
    ("54", "54"),
    ("55", "55"),
    ("56", "56"),
    ("57", "57"),
    ("58", "58"),
    ("59", "59"),
    ("60", "60"),
    ("61", "61"),
    ("62", "62"),
    ("63", "63"),
    ("64", "64"),
    ("65", "65"),
    ("66", "66"),
    ("67", "67"),
    ("68", "68"),
    ("69", "69"),
    ("70", "70"),
    ("71", "71"),
    ("72", "72"),
    ("73", "73"),
    ("74", "74"),
    ("75", "75"),
    ("76", "76"),
    ("77", "77"),
    ("78", "78"),
    ("79", "79"),
    ("80", "80"),
    ("81", "81"),
    ("82", "82"),
    ("83", "83"),
    ("84", "84"),
    ("85", "85"),
    ("86", "86"),
    ("87", "87"),
    ("88", "88"),
    ("89", "89"),
    ("90", "90"),
    ("91", "91"),
    ("92", "92"),
    ("93", "93"),
    ("94", "94"),
    ("95", "95"),
    ("96", "96"),
    ("97", "97"),
    ("98", "98"),
    ("99", "99"),
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
    # reporttitle = ReportTitleModelChoiceField(
    #     queryset=ReportTitle.objects.all(), label="Report Title", widget=forms.Select(attrs={
    #         'class': 'form-control select2bs4'
    # }))
    # department = DepartmentModelChoiceField(
    #     queryset=Department.objects.all(), label="Department Title", widget=forms.Select(attrs={
    #         'class': 'form-control select2bs4'
    # }))
    dnno = forms.CharField(label="DN No")
    effectivedate = forms.DateField(label="Effective Date", widget=forms.DateInput(attrs={
        'class': 'form-control datepick'
    }))
    reviewdate = forms.DateField(label="Review Date", widget=forms.DateInput(attrs={
        'class': 'form-control datepick'
    }))
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
    expireddate = MultiExampleField()

    class Meta:
        model = WeighingState
        fields = ['id', 'product','batchno', 'expireddate', 'operator','petugasgudang']
        widgets = {
            'status': forms.RadioSelect
        }


class WeighingStateInitialForm(ModelForm):
    expireddate = MultiExampleField()
    class Meta:
        model = WeighingState
        fields = ['id', 'product', 'batchno', 'expireddate','operator','petugasgudang']


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

class ConfigForm(ModelForm):
    class Meta:
        model = AdminConfig
        fields = ['reporttitle', 'department','weightadjustment']