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
    ("1", "Final Report"),
    ("2", "Full Report"),
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
    ("2022", "2022"),
    ("2023", "2023"),
    ("2024", "2024"),
    ("2025", "2025"),
    ("2026", "2026"),
    ("2027", "2027"),
    ("2028", "2028"),
    ("2029", "2029"),
    ("2030", "2030"),
    ("2031", "2031"),
    ("2032", "2032"),
    ("2033", "2033"),
    ("2034", "2034"),
    ("2035", "2035"),
    ("2036", "2036"),
    ("2037", "2037"),
    ("2038", "2038"),
    ("2039", "2039"),
    ("2040", "2040"),
    ("2041", "2041"),
    ("2042", "2042"),
    ("2043", "2043"),
    ("2044", "2044"),
    ("2045", "2045"),
    ("2046", "2046"),
    ("2047", "2047"),
    ("2048", "2048"),
    ("2049", "2049"),
    ("2050", "2050"),
    ("2051", "2051"),
    ("2052", "2052"),
    ("2053", "2053"),
    ("2054", "2054"),
    ("2055", "2055"),
    ("2056", "2056"),
    ("2057", "2057"),
    ("2058", "2058"),
    ("2059", "2059"),
    ("2060", "2060"),
    ("2061", "2061"),
    ("2062", "2062"),
    ("2063", "2063"),
    ("2064", "2064"),
    ("2065", "2065"),
    ("2066", "2066"),
    ("2067", "2067"),
    ("2068", "2068"),
    ("2069", "2069"),
    ("2070", "2070"),
    ("2071", "2071"),
    ("2072", "2072"),
    ("2073", "2073"),
    ("2074", "2074"),
    ("2075", "2075"),
    ("2076", "2076"),
    ("2077", "2077"),
    ("2078", "2078"),
    ("2079", "2079"),
    ("2080", "2080"),
    ("2081", "2081"),
    ("2082", "2082"),
    ("2083", "2083"),
    ("2084", "2084"),
    ("2085", "2085"),
    ("2086", "2086"),
    ("2087", "2087"),
    ("2088", "2088"),
    ("2089", "2089"),
    ("2090", "2090"),
    ("2091", "2091"),
    ("2092", "2092"),
    ("2093", "2093"),
    ("2094", "2094"),
    ("2095", "2095"),
    ("2096", "2096"),
    ("2097", "2097"),
    ("2098", "2098"),
    ("2099", "2099"),
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
        queryset=Department.objects.all(), label="Department Title", widget=forms.Select(attrs={
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
    expireddate = MultiExampleField()

    class Meta:
        model = WeighingState
        fields = ['id', 'product','batchno','jumlahkoli', 'expireddate', 'operator','petugasgudang']
        widgets = {
            'status': forms.RadioSelect
        }


class WeighingStateInitialForm(ModelForm):
    expireddate = MultiExampleField()
    class Meta:
        model = WeighingState
        fields = ['id', 'product', 'batchno','jumlahkoli', 'expireddate','operator','petugasgudang']


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
