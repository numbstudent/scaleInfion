from itertools import product
from math import prod
from mainApp.models import *
from mainApp.forms import *
from django.shortcuts import get_list_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import RestrictedError, Sum, Q, F
from django.db.models.functions import Coalesce
from django.contrib.auth.decorators import login_required
from django import template
from django.db import IntegrityError
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
import csv
from datetime import datetime, timedelta


loginpage = 'login'

@login_required(login_url=loginpage)
def index(request):
    context = {}
    context ['state'] = WeighingState.objects.filter(status=True).first()
    return render(request, 'home.html', context=context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@csrf_exempt
def ProductView(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"message": form.errors}, status=400)

    elif request.method == "GET":
        data = Product.objects.all().order_by('name').values()
        return JsonResponse(list(data), safe=False, status=200)


@csrf_exempt
def RegisterView(request, batchno=None):
    if is_ajax(request) and request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            code = request.POST.get('code')
            boxno = request.POST.get('boxno')
            batchno = request.POST.get('batchno')
            productid = Product.objects.filter(code=code).first()
            boxexists = Register.objects.filter(product=productid, batchno=batchno, boxno=boxno).exists()
            boxkosongexists = Register.objects.filter(product=productid, batchno=batchno, status=None).exists()
            weighingstate = WeighingState.objects.filter(status=True, batchno=batchno, product=productid).exists()
            print(weighingstate)
            if not weighingstate:
                return JsonResponse({"message": "Box tidak sesuai dengan Batch."}, status=400)
            if boxexists or int(boxno) < 1:
                return JsonResponse({"message": "Box sudah diinput. Hapus box terlebih dahulu untuk mereset."}, status=400)
            elif boxkosongexists:
                return JsonResponse({"message": "Box kosong harus ditimbang terlebih dahulu."}, status=400)
            else:
                instance = form.save(commit=False)
                instance.product = productid
                instance.createdby = request.user
                instance.save()
                # ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"message": "Data berhasil diinput"}, status=200)
        else:
            return JsonResponse({"message": "Isikan parameter."}, status=400)

    elif is_ajax(request) and request.method == "GET":
        batchno = request.GET.get('batchno')
        code = request.GET.get('code')
        insertsuccess = "True"
        if batchno:
            ## kalau weight masuk tidak via mesin
            # box = insertWeight(batchno)
            # if not box['status']:
            #     insertsuccess = "False"
            data = Register.objects.annotate(product_name=F('product__name'),iot_weight=F('weight'))\
            .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight','status')\
            .filter(batchno=batchno, product__code=code).order_by('-createdon')
        else:
            data = Register.objects.all().values()
        # return JsonResponse({"insertsuccess":insertsuccess,"id":box['id'], "batch":list(data)}, safe=False, status=200)
        return JsonResponse({"insertsuccess":insertsuccess, "batch":list(data)}, safe=False, status=200)

    elif is_ajax(request) and request.method == "PUT":
        body = json.loads(request.body)
        registerid = body['registerid']
        obj = Register.objects.filter(id=registerid)
        obj.delete()
        return JsonResponse({"message": "Data berhasil dihapus"}, status=200)

@login_required(login_url=loginpage)
def ScaleSimulator(request):
    context = {}
    context['action'] = 'view'
    context['data'] = Logging.objects.all().order_by('-id')[:10]
    if request.method == "POST":
        form = SimulatorForm(request.POST)
        context['form'] = form
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lot = 1
            instance.save()
            return redirect('viewsimulator')
    else:
        context['form'] = SimulatorForm()

    return render(request, 'weighing_simulator.html', context=context)

@csrf_exempt
def ScaleView(request):
    obj = Logging.objects.latest('id')

    if request.method == "GET":
        curtime = datetime.now() - timedelta(minutes=1)
        data = Logging.objects.filter(datetime__gte=curtime).order_by('-id').values('id','weighing').first()
        # data = Logging.objects.order_by('-id').values('id','weighing').first()

        #get current weight
        activebatchno = WeighingState.objects.filter(status=True).last().batchno
        if activebatchno:
            currentbox = Register.objects.filter(batchno = activebatchno, status = None).last()
            if currentbox:
                weight = Logging.objects.filter(datetime__gte=currentbox.createdon).last()
                if weight:
                    print(activebatchno)
                    print(currentbox)
                    print(weight.status)
                    print(weight.weighing)
                    currentbox.weight = weight.weighing
                    currentbox.status = weight.status
                    currentbox.save()
        return JsonResponse(data, safe=False, status=200)

def insertWeight(batchno):
    # curtime = datetime.now() - timedelta(seconds=5)
    measuredbox = {}
    measuredbox['status']=True
    measuredbox['id'] = None
    newweight = Logging.objects.all().\
        order_by('-id').values_list('id', 'weighing')
        # .filter(datetime__gte=curtime)\
    
    unweighted = Register.objects.filter(batchno=batchno, status=None)
    if unweighted.exists():
        newweight = newweight.filter(datetime__gte=unweighted.values().first()['createdon'])
    if newweight.exists() and unweighted.exists():
        if newweight.first()[1] > 0:
            weightid = newweight.first()[0]
            obj = unweighted.first()
            print(obj.product.minweight)
            print(obj.product.maxweight)
            print(newweight.first()[1])
            if newweight.first()[1] >= obj.product.minweight and newweight.first()[1] <= obj.product.maxweight:
                obj.status = True
                obj.weight_id = weightid
                obj.save()
                measuredbox['status'] = True
                measuredbox['id'] = obj.id
                # print("Data memenuhi syarat beban.")
            else:
                obj.status = None
                obj.weight_id = weightid
                obj.save()
                measuredbox['status'] = None
                measuredbox['id'] = obj.id
                # print("Error: Data tidak memenuhi syarat beban. (weight=" +
                #       str(newweight.first()[1])+",min="+str(obj.product.minweight)+"max="+str(obj.product.maxweight))
    return measuredbox


@login_required(login_url=loginpage)
def viewProduct(request):
    context = {}
    context['action'] = 'view'
    context['data'] = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('viewproduct')
    else:
        context['form'] = ProductForm()

    return render(request, 'master_product.html', context=context)


@login_required(login_url=loginpage)
def deleteProduct(request, id):
    obj = Product.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewproduct')

@login_required(login_url=loginpage)
def editProduct(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        obj = Product.objects.get(id=id)
        form = ProductForm(instance=obj)
        context['data'] = Product.objects.all()
        context['form'] = form
    if request.method == 'POST':
        obj = Product.objects.get(id=id)
        form = ProductForm(request.POST, instance=obj)
        context['data'] = Product.objects.all()
        context['form'] = form
        if form.is_valid():
            obj.name = form.cleaned_data.get('name')
            obj.code = form.cleaned_data.get('code')
            obj.minweight = form.cleaned_data.get('minweight')
            obj.maxweight = form.cleaned_data.get('maxweight')
            obj.status = form.cleaned_data.get('status')
            obj.save()
            context['message'] = "Data berhasil disimpan."
            return redirect('viewproduct')
    return render(request, 'master_product.html', context=context)


@login_required(login_url=loginpage)
def viewDepartment(request):
    context = {}
    context['action'] = 'view'
    context['data'] = Department.objects.all()
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        context['form'] = form
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.POST.get('name').upper()
            instance.save()
            return redirect('viewdepartment')
    else:
        context['form'] = DepartmentForm()

    return render(request, 'master_department.html', context=context)


@login_required(login_url=loginpage)
def deleteDepartment(request, id):
    obj = Department.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewdepartment')

@login_required(login_url=loginpage)
def editDepartment(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        obj = Department.objects.get(id=id)
        form = DepartmentForm(instance=obj)
        context['data'] = Department.objects.all()
        context['form'] = form
    if request.method == 'POST':
        obj = Department.objects.get(id=id)
        form = DepartmentForm(request.POST, instance=obj)
        context['data'] = Department.objects.all()
        context['form'] = form
        if form.is_valid():
            obj.name = form.cleaned_data.get('name').upper()
            obj.save()
            context['message'] = "Data berhasil disimpan."
            return redirect('viewdepartment')
    return render(request, 'master_department.html', context=context)


@login_required(login_url=loginpage)
def viewReportBody(request):
    context = {}
    context['action'] = 'view'
    context['data'] = Report.objects.all()
    if request.method == "POST":
        form = ReportBodyForm(request.POST)
        context['form'] = form
        if form.is_valid():
            # instance = form.save(commit=False)
            batchnoid = request.POST.get('batchno')
            product = Product.objects.get(weighingstate__id=batchnoid)
            batchno = WeighingState.objects.filter(id=batchnoid).values('batchno').first()['batchno']
            print(batchno)
            reporttitle = ReportTitle.objects.get(id=request.POST.get('reporttitle'))
            department = Department.objects.get(id=request.POST.get('department'))
            reviewdate = request.POST.get('reviewdate')
            effectivedate = request.POST.get('effectivedate')
            dnno = request.POST.get('dnno')
            dnrev = request.POST.get('dnrev')
            
            obj = Report(product=product, batchno=batchno, reporttitle=reporttitle, department=department,
                   reviewdate=reviewdate, effectivedate=effectivedate, dnno=dnno, dnrev=dnrev)

            obj.save()
            return redirect('viewreportbody')
    else:
        context['form'] = list(ReportBodyForm())

    return render(request, 'report_body.html', context=context)


@login_required(login_url=loginpage)
def deleteReportBody(request, id):
    obj = Report.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewreportbody')

@login_required(login_url=loginpage)
def editReportBody(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        obj = Report.objects.get(id=id)
        form = ReportBodyForm(instance=obj)
        context['data'] = Report.objects.all()
        context['form'] = list(form)
    if request.method == 'POST':
        obj = Report.objects.get(id=id)
        form = ReportBodyForm(request.POST, instance=obj)
        context['data'] = Report.objects.all()
        context['form'] = list(form)
        if form.is_valid():
            obj.title = form.cleaned_data.get('title').upper()
            obj.subtitle = form.cleaned_data.get('subtitle').upper()
            obj.save()
            context['message'] = "Data berhasil disimpan."
            return redirect('viewreportbody')
    return render(request, 'report_body.html', context=context)


@login_required(login_url=loginpage)
def viewHistory(request):
    context = {}
    datamodel = Register.objects.annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date', 'status').order_by('-input_date')
    hasFilter = False
    if request.method == "POST":
        form = ReportBatchForm(request.POST)
        product = request.POST.get('productid')
        batchno = request.POST.get('batchno')
        inputdatefrom = request.POST.get('inputdatefrom')
        inputdateto = request.POST.get('inputdateto')
        context['form'] = list(form)
        if product:
            datamodel = datamodel.filter(product=product)
        if batchno:
            datamodel = datamodel.filter(batchno=batchno)
        if inputdatefrom:
            datamodel = datamodel.filter(createdon__gte=inputdatefrom)
        if inputdateto:
            inputdateto = inputdateto + " 23:59"
            datamodel = datamodel.filter(createdon__lte=inputdateto)
        if product or batchno or inputdatefrom or inputdateto:
            hasFilter = True
    else:
        context['form'] = list(ReportBatchForm())
    if hasFilter:
       context['data'] = datamodel
    else:
       context['data'] = datamodel[:100]
    return render(request, 'history.html', context=context)


@login_required(login_url=loginpage)
def viewReportBatch(request):
    context = {}
    datamodel = Register.objects.annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date').order_by('-input_date')
    hasFilter = False
    if request.method == "POST":
        form = ReportBatchForm(request.POST)
        product = request.POST.get('productid')
        batchno = request.POST.get('batchno')
        inputdatefrom = request.POST.get('inputdatefrom')
        inputdateto = request.POST.get('inputdateto')
        context['form'] = form
        if product:
            datamodel = datamodel.filter(product=product)
        if batchno:
            datamodel = datamodel.filter(batchno=batchno)
        if inputdatefrom:
            datamodel = datamodel.filter(weight__gte=inputdatefrom)
        if inputdateto:
            inputdateto = inputdateto + " 23:59"
            datamodel = datamodel.filter(createdon__lte=inputdateto)
        if product or batchno or inputdatefrom or inputdateto:
            hasFilter = True
    else:
        context['form'] = list(ReportBatchForm())
    if hasFilter:
       context['data'] = datamodel
    else:
       context['data'] = datamodel[:100]
    return render(request, 'report_batch.html', context=context)


@csrf_exempt
def reportBatchCSV(request):
    #fetch data
    context = {}
    hasFilter = False
    datamodel = Register.objects.annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .order_by('-input_date')
    if request.method == "GET":
        form = ReportBatchForm(request.GET)
        product = request.GET.get('productid')
        batchno = request.GET.get('batchno')
        inputdatefrom = request.GET.get('inputdatefrom')
        inputdateto = request.GET.get('inputdateto')
        context['form'] = form
        if product:
            datamodel = datamodel.filter(product=product)
        if batchno:
            datamodel = datamodel.filter(batchno=batchno)
        if inputdatefrom:
            datamodel = datamodel.filter(weight__gte=inputdatefrom)
        if inputdateto:
            inputdateto = inputdateto + " 23:59"
            datamodel = datamodel.filter(createdon__lte=inputdateto)
        if product or batchno or inputdatefrom or inputdateto:
            hasFilter = True
    if hasFilter:
       context['data'] = datamodel
    else:
       context['data'] = datamodel[:100]
    #writing to csv
    output = []
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="report_batch.csv"'},
    )
    writer = csv.writer(response)
    query_set = context['data']
    #Table Header
    writer.writerow(['Product Name', 'Batch No', 'Box No', 'Weight', 'Date'])
    for record in query_set:
        output.append([record.product_name, record.batchno,
                      record.boxno, record.iot_weight, record.input_date])
    #Table Data
    writer.writerows(output)
    return response


@login_required(login_url=loginpage)
def viewReportTitle(request):
    context = {}
    context['action'] = 'view'
    context['data'] = ReportTitle.objects.all()
    if request.method == "POST":
        form = ReportTitleForm(request.POST)
        context['form'] = form
        if form.is_valid():
            instance = form.save(commit=False)
            instance.title = request.POST.get('title').upper()
            instance.subtitle = request.POST.get('subtitle').upper()
            instance.save()
            return redirect('viewreporttitle')
    else:
        context['form'] = ReportTitleForm()

    return render(request, 'master_reporttitle.html', context=context)


@login_required(login_url=loginpage)
def deleteReportTitle(request, id):
    obj = ReportTitle.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewreporttitle')

@login_required(login_url=loginpage)
def editReportTitle(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        obj = ReportTitle.objects.get(id=id)
        form = ReportTitleForm(instance=obj)
        context['data'] = ReportTitle.objects.all()
        context['form'] = form
    if request.method == 'POST':
        obj = ReportTitle.objects.get(id=id)
        form = ReportTitleForm(request.POST, instance=obj)
        context['data'] = ReportTitle.objects.all()
        context['form'] = form
        if form.is_valid():
            obj.title = form.cleaned_data.get('title').upper()
            obj.subtitle = form.cleaned_data.get('subtitle').upper()
            obj.save()
            context['message'] = "Data berhasil disimpan."
            return redirect('viewreporttitle')
    return render(request, 'master_reporttitle.html', context=context)

@login_required(login_url=loginpage)
def reportBatchPDF(request):
    from django.core.files.storage import FileSystemStorage
    from django.http import HttpResponse
    from django.template.loader import render_to_string
    from weasyprint import HTML

    datamodel = Register.objects.order_by('boxno')
    datamodel2 = UploadedRegister.objects.order_by('boxno')
    product_name = ""
    if request.method == "GET":
        form = ReportBatchForm(request.GET)
        product = request.GET.get('productid')
        reportid = request.GET.get('id')
        header = Report.objects.all().get(id=reportid)
        datamodel = datamodel.filter(batchno=header.batchno, product=header.product)
        datamodel2 = datamodel2.filter(batchno=header.batchno, product=header.product)
    else:
        datamodel = datamodel[0]
        datamodel2 = datamodel2[0]
    if datamodel.count()%2 == 0:
        rowlen = datamodel.count()//2
    else:
        rowlen = datamodel.count()//2+1
    # testing in windows
    return render(request, 'report_batch_pdf_template.html', context={'data': datamodel, 'data2': datamodel2, 'header': header, 'rowlen': rowlen})
    html_string = render_to_string('report_batch_pdf_template.html', {'data': datamodel, 'data2': datamodel2, 'header':header, 'rowlen':rowlen})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/REPORTBATCH.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('REPORTBATCH.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="REPORTBATCH.pdf"'
        return response

    return response

@login_required(login_url=loginpage)
def viewUploadBatch(request):
    from io import StringIO
    context = {}
    context['action'] = 'view'    
    context['data'] = UploadedRegister.objects.annotate(product_name=F('product__name'))\
    .values('id','product_name','batchno','boxno','weight','measuredate')\
    .order_by('-createdon')
    if request.method == "POST":
        form = UploadBatchForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            productid = request.POST.get('productid')
            product = Product.objects.get(id=productid)
            batchno = request.POST.get('batchno')
            file = request.FILES['file'].read().decode('utf-8')
            reader = csv.reader(StringIO(file), delimiter=',')
            next(reader) #skip header
            for row in reader:
                measuredate = row[2]
                measuredate = measuredate.split("/")
                measuredate = [measuredate[2],measuredate[1],measuredate[0]]
                measuredate = "-".join(measuredate)
                obj = UploadedRegister(product=product, batchno=batchno, boxno=row[0], weight=row[1], measuredate=measuredate)
                obj.save()
            return redirect('viewuploadbatch')
    else:
        context['form'] = UploadBatchForm()

    return render(request, 'upload_batch.html', context=context)

@login_required(login_url=loginpage)
def deleteUploadBatch(request, id):
    obj = UploadedRegister.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewuploadbatch')

@login_required(login_url=loginpage)
def viewWeighingState(request): #startbatch
    context = {}
    context['action'] = 'view'
    context['data'] = WeighingState.objects.filter(id=1, status=True)
    noState = WeighingState.objects.filter(id=1, status=True).exists()
    if not noState and request.method == "POST":
        form = WeighingStateForm(request.POST)
        context['form'] = form
        if form.is_valid():
            dataexist = WeighingState.objects.filter(id=1).exists()
            if dataexist:
                obj = WeighingState.objects.get(id=1)
                obj.product = form.cleaned_data.get('product')
                obj.batchno = form.cleaned_data.get('batchno')
            else:
                obj = WeighingState(id=1, product=form.cleaned_data.get(
                    'product'), batchno=form.cleaned_data.get('batchno'))
            # obj.status = form.cleaned_data.get('status')
            obj.status = 1
            obj.save()
            return redirect('startbatch')
    else:
        context['form'] = WeighingStateForm()

    return render(request, 'weighingstate.html', context=context)

@login_required(login_url=loginpage)
def viewEndBatch(request): #endbatch
    context = {}
    context['action'] = 'view'
    context['data'] = WeighingState.objects.filter()
    noState = WeighingState.objects.filter(id=1, status=False).exists()
    if not noState and request.method == "POST":
        form = WeighingStateForm(request.POST)
        context['form'] = form
        if form.is_valid():
            obj = WeighingState.objects.get(id=1)
            obj.product = form.cleaned_data.get('product')
            # obj.status = form.cleaned_data.get('status')
            obj.status = 0
            obj.save()
            return redirect('endbatch')
    else:
        activestate = WeighingState.objects.filter().values('product','batchno','pendingstatus').first()
        batchno = activestate['batchno']
        productid = activestate['product']
        form = WeighingStateForm()
        # form.fields["product"].queryset = Product.objects.filter(id=1)
        # form.fields["batchno"].initial = batchno
        context['form'] = form

    return render(request, 'end_batch.html', context=context)

@csrf_exempt
def RejectBox(request):
    if request.method == "POST":
        form = RejectForm(request.POST)
        id = request.POST.get('id')
        status = request.POST.get('status')
        print(request.POST)
        if form.is_valid():
            boxexists = Register.objects.filter(id=id).exists()
            if not boxexists:
                return JsonResponse({"message": "Box tidak ditemukan."}, status=400)
            else:
                instance = Register.objects.filter(id=id).first()
                instance.status = status
                instance.save()
                return JsonResponse({"message": "Data berhasil diinput"}, status=200)
        else:
            return JsonResponse({"message": "Isikan parameter."}, status=400)
    else:
        return JsonResponse({"message": "Bad Request."}, status=400)



@login_required(login_url=loginpage)
def viewWeighingState(request):
    context = {}
    context['action'] = 'view'
    context['data'] = WeighingState.objects.all()
    if request.method == "POST":
        form = WeighingStateInitialForm(request.POST)
        context['form'] = form
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pendingstatus = True
            instance.status = False
            instance.batchno = form.cleaned_data.get('batchno').upper()
            # batchnoobj = WeighingState.objects.all()
            # batchnoobj.update(status=False)
            instance.save()
            return redirect('viewweighingstate')
    else:
        form = WeighingStateInitialForm()
        context['form'] = form

    return render(request, 'weighingstate.html', context=context)


@login_required(login_url=loginpage)
def deleteWeighingState(request, id):
    obj = WeighingState.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewweighingstate')

@login_required(login_url=loginpage)
def editWeighingState(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateForm(instance=obj)
        context['data'] = WeighingState.objects.all()
        context['form'] = list(form)
    if request.method == 'POST':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateForm(request.POST, instance=obj)
        context['data'] = WeighingState.objects.all()
        context['form'] = list(form)
        if form.is_valid():
            # obj.title = form.cleaned_data.get('title').upper()
            obj.batchno = form.cleaned_data.get('batchno').upper()
            obj.save()
            context['message'] = "Data berhasil disimpan."
            return redirect('viewWeighingState')
    return render(request, 'weighingstate.html', context=context)

@login_required(login_url=loginpage)
def activateWeighingState(request, id, status):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        if status == 'activate':
            batchnoobj = WeighingState.objects.filter(status=True)
            batchnoobj.update(status=False)
            obj = WeighingState.objects.filter(id=id)
            obj.update(status=True)
        elif status == 'deactivate':
            obj = WeighingState.objects.filter(id=id)
            obj.update(status=False)
        return redirect('viewweighingstate')


@login_required(login_url=loginpage)
def closeWeighingState(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None
    if request.method == 'GET':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateCloseForm(instance=obj)
        form.fields["spvpabrik"].queryset = User.objects.filter(
            groups__name='supervisorpabrik')
        form.fields["spvgudang"].queryset = User.objects.filter(
            groups__name='supervisorgudang')
        context['data'] = WeighingState.objects.all()
        context['form'] = list(form)
    if request.method == 'POST':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateCloseForm(request.POST, instance=obj)
        context['data'] = WeighingState.objects.all()
        context['form'] = list(form)
        if form.is_valid():
            obj.spvpabrik = form.cleaned_data.get('spvpabrik')
            obj.spvgudang = form.cleaned_data.get('spvgudang')
            obj.pendingstatus = False
            obj.save()
            context['message'] = "Data berhasil disimpan."
            return redirect('viewweighingstate')
    return render(request, 'weighingstateclose.html', context=context)


@login_required(login_url=loginpage)
def viewBatchHistory(request, batchno):
    context = {}
    datamodel = Register.objects.filter(batchno=batchno).annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date', 'status').order_by('-input_date')
    context['data'] = datamodel
    return render(request, 'batchno_history.html', context=context)
