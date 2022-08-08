import code
from itertools import product
from math import prod
from mainApp.models import *
from mainApp.forms import *
from secureapp.decorators import allowed_users, allowed_check, allowed_check_function
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
def front(request):
    context = {}
    return render(request, 'frontpage.html', context=context)

@login_required(login_url=loginpage)
@allowed_check(feature_alias='weighing')
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
            boxexists = Register.objects.filter(product=productid, batchno=batchno, boxno=boxno).exclude(status=0).exists()
            boxkosongexists = Register.objects.filter(product=productid, batchno=batchno, status=None).exists()
            weighingstate = WeighingState.objects.filter(status=True, batchno=batchno, product=productid).exists()
            print(boxexists)
            if not weighingstate:
                return JsonResponse({"message": "Box tidak sesuai dengan Batch."}, status=400)
            # if boxexists or int(boxno) < 1:
            #     return JsonResponse({"message": "Box sudah diinput. Hapus box terlebih dahulu untuk mereset."}, status=400)
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
            .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight','status','createdon')\
            .filter(batchno=batchno, product__code=code).order_by('-createdon')
        else:
            data = Register.objects.all().values()
        # return JsonResponse({"insertsuccess":insertsuccess,"id":box['id'], "batch":list(data)}, safe=False, status=200)
        return JsonResponse({"insertsuccess":insertsuccess, "batch":list(data)}, safe=False, status=200)

    elif is_ajax(request) and request.method == "PUT":
        group = request.user.groups.all()[0].name
        privilegecheck = allowed_check_function('managebatch',request)
        if privilegecheck:
            body = json.loads(request.body)
            registerid = body['registerid']
            obj = Register.objects.filter(id=registerid)
            obj.delete()
            return JsonResponse({"message": "Data berhasil dihapus"}, status=200)
        else:
            error_message = 'Anda tidak memiliki akses untuk ini!'
            return JsonResponse({"message": error_message}, status=200)

@csrf_exempt
def editRegisterWeight(request):
    group = request.user.groups.all()[0].name
    privilegecheck = allowed_check_function('managebatch',request)
    if privilegecheck:
        if request.method == "POST":
            body = json.loads(request.body)
            registerid = body['registerid']
            finalweight = body['finalweight']
            obj = Register.objects.filter(id=registerid).first()
            message = ""
            if(((finalweight - obj.weight) < 1) and ((finalweight - obj.weight) > -1)):
                obj.weight = finalweight
                obj.save()
                message = "Perubahan selesai."
            else:
                message = "Perubahan data melebihi 1 gram!"
            return JsonResponse({"message": message}, status=200)
    else:
        error_message = 'Anda tidak memiliki akses untuk ini!'
        return JsonResponse({"message": error_message}, status=200)
    

@login_required(login_url=loginpage)
@allowed_check(feature_alias='simulator')
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
    configcheck = AdminConfig.objects.all().exists()
    if not configcheck:
        obj = AdminConfig(spvinterrupt=False)
        obj.save()
    if request.method == "GET":
        curtime = datetime.now() - timedelta(minutes=1)
        data = Logging.objects.filter(datetime__gte=curtime).order_by('-id').values('id','weighing').first()
        # data = Logging.objects.order_by('-id').values('id','weighing').first()

        #get current weight
        activebatchno = WeighingState.objects.filter(status=True).last().batchno
        weightadjustment = AdminConfig.objects.last().weightadjustment
        if activebatchno:
            currentbox = Register.objects.filter(batchno = activebatchno, status = None).last()
            if currentbox:
                weight = Logging.objects.filter(datetime__gte=currentbox.createdon).last()
                if weight:
                    print(activebatchno)
                    print(currentbox)
                    print(weight.status)
                    print(weight.weighing)
                    currentbox.weight = weight.weighing + weightadjustment
                    currentbox.status = weight.status
                    currentbox.save()
        return JsonResponse(data, safe=False, status=200)

@csrf_exempt
def SupervisorApproval(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')

        print(json.loads(body_unicode))
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']

        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=password)
        if user is not None:
            group = user.groups.all()[0].name
            if str.__contains__(group, 'supervisor'):
            # if str.__contains__(group, 'supervisor') or str.__contains__(group, 'administrator'):
                expireddate = datetime.now() + timedelta(minutes=1)
                config = AdminConfig.objects.first()
                config.spvapproval = True
                config.spvapprovalexpireddate = expireddate
                config.save()
                return JsonResponse({"message": "Akses Supervisor diberikan."}, status=200)
            else:
                return JsonResponse({"message": "Hanya akun Supervisor / Administrator yang diperbolehkan!"}, status=400)    
        else:
            return JsonResponse({"message": "Username / Password salah!"}, status=400)

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
@allowed_check(feature_alias='masterproduct')
def viewUploadProduct(request):
    from io import StringIO
    context = {}
    context['action'] = 'upload'    
    # context['data'] = ProductUploadTemp.objects.all()
    context['data'] = ProductUploadTemp.objects.raw('SELECT t.*, p.code cur_code, p.name cur_name, p.maxweight cur_maxweight, \
        p.minweight cur_minweight, p.standardweight cur_standardweight,  \
        case when p.code is null then \'New Data\'\
        when t.name <> p.name or t.maxweight <> p.maxweight or t.minweight <> p.minweight or t.standardweight <> p.standardweight \
        then \'Update\' else \'\'\
        end description\
        FROM mainApp_productuploadtemp t\
        left join mainApp_product p on t.code = p.code \
        order by description desc')
    if request.method == "POST":
        form = UploadProductForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            file = request.FILES['file'].read().decode('utf-8')
            reader = csv.reader(StringIO(file), delimiter=',')
            next(reader) #skip header
            ProductUploadTemp.objects.all().delete()
            for row in reader:
                obj = ProductUploadTemp(code=row[0], name=row[1], minweight=row[2],
                                        maxweight=row[3], standardweight=row[4], createdby=request.user)
                obj.save()
            return redirect('uploadproduct')
    else:
        context['form'] = UploadProductForm()

    return render(request, 'upload_product.html', context=context)


@login_required(login_url=loginpage)
@allowed_check(feature_alias='masterproduct')
def updateProductByTemporary(request):
    from io import StringIO
    context = {}
    context['action'] = 'update'    
    # context['data'] = ProductUploadTemp.objects.all()
    data = ProductUploadTemp.objects.raw('SELECT t.* \
        FROM mainApp_productuploadtemp t \
        left join mainApp_product p on t.code = p.code \
        where p.code is null or t.name <> p.name or t.maxweight <> p.maxweight or \
        t.minweight <> p.minweight or t.standardweight <> p.standardweight')

    for item in data:
        p = Product.objects.filter(code=item.code).first()
        if p:
            h = ProductHistory(code=p.code, name=p.name, maxweight=p.maxweight, minweight=p.minweight, standardweight=p.standardweight,
                            createdon=p.createdon, updatedon=p.updatedon, status=p.status, createdby=p.createdby, updatedby=p.updatedby)
            h.save()
        obj, created = Product.objects.update_or_create(
            code=item.code,
            defaults={'name': item.name, 'maxweight': item.maxweight,
                      'minweight': item.minweight, 'standardweight': item.standardweight, 'createdby': request.user},
        )
        ProductUploadTemp.objects.all().delete()

    return redirect('uploadproduct')


@login_required(login_url=loginpage)
# @allowed_check(feature_alias='masterproduct')
def downloadProductCSV(request):
    #fetch data
    context = {}
    hasFilter = False
    datamodel = Product.objects.all()
    #writing to csv
    output = []
    response = HttpResponse(
    )
    response['Content-Disposition'] = 'attachment; filename="master_product_'+str(datetime.now())+'.csv"'

    writer = csv.writer(response)
    query_set = datamodel
    #Table Header
    writer.writerow(['Code', 'Product Name', 'Min. Weight (gram)', 'Max. Weight (gram)', 'Std. Weight (gram)'])
    for record in query_set:
        output.append([record.code, record.name,
                      record.minweight, record.maxweight, record.standardweight])
    #Table Data
    writer.writerows(output)
    return response

@login_required(login_url=loginpage)
@allowed_check(feature_alias='masterproduct')
def viewProduct(request):
    context = {}
    context['action'] = 'view'
    context['data'] = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        context['form'] = form
        if form.is_valid():
            instance = form.save(commit=False)
            instance.createdby = request.user
            instance.save()
            return redirect('viewproduct')
    else:
        context['form'] = ProductForm()

    return render(request, 'master_product.html', context=context)


@login_required(login_url=loginpage)
@allowed_check(feature_alias='masterproduct')
def deleteProduct(request, id):
    obj = Product.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewproduct')

@login_required(login_url=loginpage)
@allowed_check(feature_alias='masterproduct')
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
            # obj.status = form.cleaned_data.get('status')
            obj.save()
            context['message'] = "Data berhasil disimpan."
            return redirect('viewproduct')
    return render(request, 'master_product.html', context=context)


@login_required(login_url=loginpage)
@allowed_check(feature_alias='masterdepartment')
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
@allowed_check(feature_alias='masterdepartment')
def deleteDepartment(request, id):
    obj = Department.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewdepartment')

@login_required(login_url=loginpage)
@allowed_check(feature_alias='masterdepartment')
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
@allowed_check(feature_alias='reportpdf')
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
            prevreportexist = ReportRegister.objects.filter(batchno=batchno, product=product).exists()
            dnrev = 0
            # print(prevreportexist)
            # print(Report.objects.filter(batchno=batchno, product=product).values('dnrev').order_by('-dnrev').first()['dnrev'])
            if prevreportexist:
                dnrev = Report.objects.filter(batchno=batchno, product=product).values('dnrev').order_by('-dnrev').first()['dnrev']
            dnrev = dnrev+1
            # dnrev = request.POST.get('dnrev')
            
            obj = Report(product=product, batchno=batchno, reporttitle=reporttitle, department=department,
                   reviewdate=reviewdate, effectivedate=effectivedate, dnno=dnno, dnrev=dnrev)
            obj.save()

            reportobj = Report.objects.last()
            data = Register.objects.filter(batchno=reportobj.batchno, product=reportobj.product)
            for row in data:
                obj = ReportRegister(report=reportobj, dnrev=reportobj.dnrev, product=row.product, batchno=row.batchno, \
                boxno=row.boxno, status=row.status, createdon=row.createdon, weight=row.weight, createdby=row.createdby)
                obj.save()
            return redirect('viewreportbody')
    else:
        context['form'] = list(ReportBodyForm())

    return render(request, 'report_body.html', context=context)


@login_required(login_url=loginpage)
@allowed_check(feature_alias='reportpdf')
def deleteReportBody(request, id):
    obj = Report.objects.filter(id=id)

    group = request.user.groups.all()[0].name
    if group != 'operator':
        try:
            obj.delete()
        except RestrictedError:
            error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
            return HttpResponse(error_message)
        return redirect('viewreportbody')
    else:
        error_message = 'Operator tidak boleh menghapus data! <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)

@login_required(login_url=loginpage)
@allowed_check(feature_alias='reportpdf')
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
@allowed_check(feature_alias='history')
def viewHistory(request):
    context = {}
    datamodel = Register.objects.annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date', 'status').order_by('-input_date')
    hasFilter = False
    if request.method == "POST":
        form = HistoryForm(request.POST)
        product = request.POST.get('productid')
        batchno = request.POST.get('batchno')
        inputdatefrom = request.POST.get('inputdatefrom')
        inputdateto = request.GET.get('inputdateto')
        context['form'] = list(form)
        if product:
            datamodel = datamodel.filter(product=product)
        if batchno:
            datamodel = datamodel.filter(batchno__icontains=batchno)
        if inputdatefrom:
            datamodel = datamodel.filter(createdon__gte=inputdatefrom)
        if inputdateto:
            inputdateto = inputdateto + " 23:59"
            datamodel = datamodel.filter(createdon__lte=inputdateto)
        if product or batchno or inputdatefrom or inputdateto:
            hasFilter = True
    else:
        context['form'] = list(HistoryForm())
    if hasFilter:
       context['data'] = datamodel
    else:
       context['data'] = datamodel[:100]
    return render(request, 'history.html', context=context)


@login_required(login_url=loginpage)
@allowed_check(feature_alias='reportpdf')
def viewReportBatch(request):
    context = {}
    datamodel = Register.objects.filter(Q(status=1) | Q(status=2))\
        .annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date','status').order_by('-input_date')
    hasFilter = False
    if request.method == "POST":
        form = ReportBatchForm(request.POST)
        product = request.POST.get('productid')
        batchno = request.POST.get('batchno')
        inputdatefrom = request.POST.get('inputdatefrom')
        inputdateto = request.GET.get('inputdateto')
        reporttype = request.GET.get('reporttype')
        print(reporttype)
        context['form'] = form
        if product:
            datamodel = datamodel.filter(product=product)
        if batchno:
            datamodel = datamodel.filter(batchno=batchno)
        if inputdatefrom:
            datamodel = datamodel.filter(createdon__gte=inputdatefrom)
        if inputdateto:
            inputdateto = inputdateto + " 23:59"
            datamodel = datamodel.filter(createdon__lte=inputdateto)
        if reporttype == 1:
            datamodel = datamodel.filter(Q(status=1) | Q(status=2))
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
@allowed_check(feature_alias='reportcsv')
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
        reporttype = request.GET.get('reporttype')
        context['form'] = form
        if product:
            datamodel = datamodel.filter(product=product)
        if batchno:
            datamodel = datamodel.filter(batchno=batchno)
        if inputdatefrom:
            datamodel = datamodel.filter(createdon__gte=inputdatefrom)
        if inputdateto:
            inputdateto = inputdateto + " 23:59"
            datamodel = datamodel.filter(createdon__lte=inputdateto)
        if reporttype == 1:
            datamodel = datamodel.filter(Q(status=1) | Q(status=2))
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
@allowed_check(feature_alias='masterreport')
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
@allowed_check(feature_alias='masterreport')
def deleteReportTitle(request, id):
    obj = ReportTitle.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewreporttitle')

@login_required(login_url=loginpage)
@allowed_check(feature_alias='masterreport')
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
@allowed_check(feature_alias='reportpdf')
def reportBatchPDF(request):
    from django.core.files.storage import FileSystemStorage
    from django.http import HttpResponse
    from django.template.loader import render_to_string
    from weasyprint import HTML

    
    # datamodel = Register.objects.order_by('boxno')
    datamodel = ReportRegister.objects.order_by('boxno')
    datamodel2 = UploadedRegister.objects.order_by('boxno')
    group = request.user.groups.all()[0].name
    if group != 'administrator':
        datamodel = datamodel.filter(Q(status=1) | Q(status=2))

    product_name = ""
    if request.method == "GET":
        form = ReportBatchForm(request.GET)
        product = request.GET.get('productid')
        reportid = request.GET.get('id')
        header = Report.objects.all().get(id=reportid)
        # datamodel = datamodel.filter(batchno=header.batchno, product=header.product)
        datamodel = datamodel.filter(report = header)
        datamodel2 = datamodel2.filter(batchno=header.batchno, product=header.product)
        signature = WeighingState.objects.filter(batchno=header.batchno, product=header.product).first()
    else:
        datamodel = datamodel[0]
        datamodel2 = datamodel2[0]
    if datamodel.count()%2 == 0:
        rowlen = datamodel.count()//2
    else:
        rowlen = datamodel.count()//2+1
    # testing in windows
    return render(request, 'report_batch_pdf_template2.html', context={'data': datamodel, 'data2': datamodel2, 'header': header, 'rowlen': rowlen, 'signature':signature})
    html_string = render_to_string('report_batch_pdf_template.html', {'data': datamodel, 'data2': datamodel2, 'header':header, 'rowlen':rowlen, 'signature':signature})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/REPORTBATCH.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('REPORTBATCH.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="REPORTBATCH.pdf"'
        return response

    return response

@login_required(login_url=loginpage)
@allowed_check(feature_alias='viewendbatch')
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
@allowed_check(feature_alias='managebatch')
def deleteUploadBatch(request, id):
    obj = UploadedRegister.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewuploadbatch')

# @login_required(login_url=loginpage)
# @allowed_check(feature_alias='viewendbatch')
# def viewWeighingState(request): #startbatch
#     context = {}
#     context['action'] = 'view'
#     context['data'] = WeighingState.objects.filter(id=1, status=True)
#     noState = WeighingState.objects.filter(id=1, status=True).exists()
#     if not noState and request.method == "POST":
#         form = WeighingStateForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             dataexist = WeighingState.objects.filter(id=1).exists()
#             if dataexist:
#                 obj = WeighingState.objects.get(id=1)
#                 obj.product = form.cleaned_data.get('product')
#                 obj.batchno = form.cleaned_data.get('batchno')
#             else:
#                 obj = WeighingState(id=1, product=form.cleaned_data.get(
#                     'product'), batchno=form.cleaned_data.get('batchno'))
#             # obj.status = form.cleaned_data.get('status')
#             obj.status = 1
#             obj.save()
#             return redirect('startbatch')
#     else:
#         context['form'] = WeighingStateForm()

#     return render(request, 'weighingstate.html', context=context)

@login_required(login_url=loginpage)
@allowed_check(feature_alias='viewendbatch')
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
@allowed_check(feature_alias='viewendbatch')
def viewWeighingState(request):
    context = {}
    context['action'] = 'view'
    context['data'] = WeighingState.objects.all()
    if request.method == "POST":
        privilegecheck = allowed_check_function('managebatch',request)
        print(privilegecheck)
        if privilegecheck:
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
            return HttpResponse('Anda tidak diizinkan untuk melihat halaman ini. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>')
    else:
        form = WeighingStateInitialForm()
        context['form'] = form

    return render(request, 'weighingstate.html', context=context)


@login_required(login_url=loginpage)
@allowed_check(feature_alias='managebatch')
def deleteWeighingState(request, id):
    obj = WeighingState.objects.filter(id=id)
    try:
        obj.delete()
    except RestrictedError:
        error_message = 'Data ini tidak dapat dihapus karena sedang digunakan oleh data lain. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>'
        return HttpResponse(error_message)
    return redirect('viewweighingstate')

@login_required(login_url=loginpage)
@allowed_check(feature_alias='managebatch')
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
            return redirect('viewweighingstate')
    return render(request, 'weighingstate.html', context=context)

@login_required(login_url=loginpage)
@allowed_check(feature_alias='managebatch')
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
@allowed_check(feature_alias='viewendbatch')
def closeWeighingState(request, id):
    context = {}
    context['action'] = 'edit'
    context['id'] = id
    context['message'] = None

    group = request.user.groups.all()[0].name

    if request.method == 'GET':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateCloseForm(user=request.user,instance=obj)

        if group == 'supervisorgudang':
            form.fields["spvgudang"].queryset = User.objects.filter(
                id = request.user.id)
        elif group == 'supervisorproduksi':
            form.fields["spvpabrik"].queryset = User.objects.filter(
                id=request.user.id)
        elif group == 'administrator':
            form.fields["spvgudang"].queryset = User.objects.filter(
                groups__name='supervisorgudang')
            form.fields["spvpabrik"].queryset = User.objects.filter(
                groups__name='supervisorproduksi')

        context['data'] = WeighingState.objects.all()
        context['form'] = list(form)
    if request.method == 'POST':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateCloseForm(request.POST, user=request.user, instance=obj)
        context['data'] = WeighingState.objects.all()
        context['form'] = list(form)
        if form.is_valid():
            if group == 'supervisorgudang':
                obj.spvgudang = form.cleaned_data.get('spvgudang')
            elif group == 'supervisorproduksi':
                obj.spvpabrik = form.cleaned_data.get('spvpabrik')
            elif group == 'administrator':
                obj.spvgudang = form.cleaned_data.get('spvgudang')
                obj.spvpabrik = form.cleaned_data.get('spvpabrik')
            obj.save()
            reselectobj = WeighingState.objects.get(id=id)
            if reselectobj.spvpabrik != None and reselectobj.spvgudang != None:
                reselectobj.pendingstatus = False
                reselectobj.save()
            context['message'] = "Data berhasil disimpan."
            return redirect('viewweighingstate')
    return render(request, 'weighingstateclose.html', context=context)


@login_required(login_url=loginpage)
@allowed_check(feature_alias='viewendbatch')
def viewBatchHistory(request, batchno):
    context = {}
    datamodel = Register.objects.filter(batchno=batchno).annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date', 'status').order_by('-input_date')
    context['data'] = datamodel
    return render(request, 'batchno_history.html', context=context)
