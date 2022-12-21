import code
from itertools import product
from math import prod
from mainApp.models import *
from mainApp.forms import *
from secureapp.decorators import allowed_users, allowed_check, allowed_check_function
from secureapp.models import AccessList
from django.shortcuts import get_list_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import RestrictedError, Sum, Q, F
from django.db.models.functions import Coalesce
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django import template
from django.db import IntegrityError
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .conveyor import run_conveyor
from .relay2off import relay_off
from .relay2on import relay_on
from .relay3off import relay3_off
from .relay3on import relay3_on
import json
import csv
from datetime import datetime, timedelta
from django.contrib import messages


loginpage = 'login'


@login_required(login_url=loginpage)
def front(request):
    userexists = User.objects.all().exists()
    groupexists = Group.objects.all().exists()
    accesslistexists = AccessList.objects.all().exists()
    if not groupexists:
        new_group, created = Group.objects.get_or_create(name='administrator')
        new_group, created = Group.objects.get_or_create(name='supervisorgudang')
        new_group, created = Group.objects.get_or_create(name='supervisorproduksi')
        new_group, created = Group.objects.get_or_create(name='supervisorppic')
        new_group, created = Group.objects.get_or_create(name='operator')
    if not accesslistexists:
        new_group, created = AccessList.objects.get_or_create(feature_alias='weighing', feature_name='Weighing')
        new_group, created = AccessList.objects.get_or_create(feature_alias='simulator', feature_name='Simulator')
        new_group, created = AccessList.objects.get_or_create(feature_alias='masterproduct', feature_name='Master Product')
        new_group, created = AccessList.objects.get_or_create(feature_alias='masterdepartment', feature_name='Master Department')
        new_group, created = AccessList.objects.get_or_create(feature_alias='masterreport', feature_name='Master Report')
        new_group, created = AccessList.objects.get_or_create(feature_alias='history', feature_name='History')
        new_group, created = AccessList.objects.get_or_create(feature_alias='reportcsv', feature_name='Report CSV')
        new_group, created = AccessList.objects.get_or_create(feature_alias='reportpdf', feature_name='Report PDF')
        new_group, created = AccessList.objects.get_or_create(feature_alias='managebatch', feature_name='Manage Batch')
        new_group, created = AccessList.objects.get_or_create(feature_alias='viewendbatch', feature_name='View and End Batch')
    if not userexists:        
        user = User.objects.create_user('admininfion', 'admin@admin.com', 'admin')
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        my_group = Group.objects.get(name='administrator') 
        my_group.user_set.add(user)
    configcheck = AdminConfig.objects.all().exists()
    if not configcheck:
        obj = AdminConfig(spvapproval=False)
        obj.save()
    obj = AdminConfig.objects.first()
    obj.spvapproval = False
    obj.operator = None
    obj.petugasgudang = None
    obj.save()
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
def OperatorListView(request):
    if request.method == "GET":
        data = User.objects.filter(groups__name='operator').values('first_name', 'last_name', 'username')        
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
            boxexists = Register.objects.filter(product=productid, batchno=batchno, boxno=boxno).filter(Q(status=1) | Q(status=3)).exists()
            boxrejectexists = Register.objects.filter(product=productid, batchno=batchno, boxno=boxno).filter(status=2).exists()
            boxkosongexists = Register.objects.filter(product=productid, batchno=batchno, status=None).exists()
            weighingstate = WeighingState.objects.filter(status=True, batchno=batchno, product=productid).exists()
            
            if not weighingstate:
                return JsonResponse({"message": "Box tidak sesuai dengan Batch."}, status=400)
            else:
                # operator = WeighingState.objects.filter(status=True, batchno=batchno, product=productid).first().operator
                # petugasgudang = WeighingState.objects.filter(status=True, batchno=batchno, product=productid).first().petugasgudang
                operator = AdminConfig.objects.first().operator
                petugasgudang = AdminConfig.objects.first().petugasgudang
                spvapproval = AdminConfig.objects.first().spvapproval
                if (not operator) or (not petugasgudang):
                    return JsonResponse({"message": "Isikan nama operator terlebih dahulu."}, status=400)
                elif boxexists or int(boxno) < 1:
                    return JsonResponse({"message": "Box ini sudah pernah diinput!"}, status=400)
                elif boxkosongexists:
                    return JsonResponse({"message": "Box kosong harus ditimbang terlebih dahulu."}, status=400)
                elif boxrejectexists:
                    if spvapproval:
                        # save register history
                        obj = Register.objects.filter(
                            product=productid, batchno=batchno, boxno=boxno).filter(status=2).last()
                        obj2 = RegisterHistory(
                            product=obj.product,
                            batchno=obj.batchno,
                            boxno=obj.boxno,
                            status=obj.status,
                            createdon=obj.createdon,
                            updatedon=obj.updatedon,
                            weight=obj.weight,
                            operator=obj.operator,
                            petugasgudang=obj.petugasgudang,
                            createdby=obj.createdby,
                            updatedby=obj.updatedby,
                            printedon=obj.printedon,
                            action="delete reject"
                        )
                        obj2.save()
                        # delete rejected box
                        boxreject = Register.objects.filter(product=productid, batchno=batchno, boxno=boxno).filter(status=2).last()
                        boxreject.delete()
                        config = AdminConfig.objects.first()
                        config.spvapproval = False
                        config.save()
                        # save new record
                        instance = form.save(commit=False)
                        instance.product = productid
                        instance.createdby = request.user
                        instance.operator = operator
                        instance.petugasgudang = petugasgudang.title()
                        instance.save()
                        # ser_instance = serializers.serialize('json', [instance, ])
                        # boxreject = Register.objects.filter(product=productid, batchno=batchno, boxno=boxno).filter(status=2).last()
                        # obj = Register(product=productid, batchno=batchno, boxno=boxno, createdby = request.user, operator = operator, petugasgudang = petugasgudang, weight = boxreject.weight, status=3)
                        # obj.save()
                        # config = AdminConfig.objects.first()
                        # config.spvapproval = False
                        # config.save()
                        # return JsonResponse({"message": "Input last box dengan persetujuan supervisor berhasil ditambahkan."}, status=200)
                        result = relay_on()
                        if result:
                            msg = "Relay 3 On!"
                        else:
                            msg = "Relay 3 tidak dapat berjalan!"
                        import time
                        time.sleep(5)
                        result = relay_on()
                        if result:
                            msg = msg+" Relay 3 Off!"
                        else:
                            msg = msg+" Relay 3 tidak dapat berjalan!"
                        return JsonResponse({"message": "Data berhasil diinput. "+msg}, status=200)
                    else :
                        return JsonResponse({"message": "Box ini sudah pernah diinput!"}, status=400)
                else:
                    instance = form.save(commit=False)
                    instance.product = productid
                    instance.createdby = request.user
                    instance.operator = operator
                    instance.petugasgudang = petugasgudang.title()
                    instance.save()

                    # ser_instance = serializers.serialize('json', [instance, ])
                    return JsonResponse({"message": "Data berhasil diinput"}, status=200)
        else:
            return JsonResponse({"message": "Isikan parameter."}, status=400)

    elif request.method == "GET":
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
        spvapproval = AdminConfig.objects.first().spvapproval
        operator = AdminConfig.objects.first().operator
        petugasgudang = AdminConfig.objects.first().petugasgudang

        expireddate = AdminConfig.objects.first().spvapprovalexpireddate 
        if expireddate:
            if datetime.now() > expireddate:
                config = AdminConfig.objects.first()
                config.spvapproval = False
                config.spvapprovalexpireddate = None
                config.save()

        jumlahkoli = Register.objects.filter(batchno=batchno, product__code=code).filter(Q(status=1)).count()
        # jumlahkoli =42
        # return JsonResponse({"insertsuccess":insertsuccess,"id":box['id'], "batch":list(data)}, safe=False, status=200)
        return JsonResponse({"insertsuccess":insertsuccess, "batch":list(data), "spvapproval":spvapproval, "jumlahkoli":jumlahkoli
        , "operator":operator, "petugasgudang":petugasgudang
        }, safe=False, status=200)

    elif is_ajax(request) and request.method == "PUT":
        group = request.user.groups.all()[0].name
        privilegecheck = True
        # privilegecheck = allowed_check_function('managebatch',request)
        group = request.user.groups.all()[0].name 
        if group != 'administrator': #fungsi baru
            privilegecheck = False
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
    privilegecheck = True
    # privilegecheck = allowed_check_function('managebatch',request) #fungsi lama
    group = request.user.groups.all()[0].name 
    if group != 'administrator': #fungsi baru
        privilegecheck = False
    if privilegecheck:
        if request.method == "POST":
            body = json.loads(request.body)
            registerid = body['registerid']
            finalweight = body['finalweight']
            obj = Register.objects.filter(id=registerid).first()
            message = ""
            if(((finalweight - obj.weight) < 3) and ((finalweight - obj.weight) > -3)):
                obj.weight = finalweight
                obj.save()
                # save register history
                obj = Register.objects.filter(id=registerid).first()
                obj2 = RegisterHistory(
                    product=obj.product,
                    batchno=obj.batchno,
                    boxno=obj.boxno,
                    status=obj.status,
                    createdon=obj.createdon,
                    updatedon=obj.updatedon,
                    weight=obj.weight,
                    operator=obj.operator,
                    petugasgudang=obj.petugasgudang,
                    createdby=obj.createdby,
                    updatedby=obj.updatedby,
                    printedon=obj.printedon,
                    action="update weight"
                )
                obj2.save()
                message = "Data berhasil diubah."
            else:
                message = "Perubahan data melebihi 3 gram!"
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
    if request.method == "GET":
        curtime = datetime.now() - timedelta(minutes=1)
        data = Logging.objects.filter(datetime__gte=curtime).order_by('-id').values('id','weighing').first()
        # data = Logging.objects.order_by('-id').values('id','weighing').first()

        #get current weight
        activebatchnoexists = WeighingState.objects.filter(status=True).exists()
        activebatchno = None
        if activebatchnoexists:
            activebatchno = WeighingState.objects.filter(status=True).last().batchno
        weightadjustment = AdminConfig.objects.last().weightadjustment
        if activebatchno:
            currentbox = Register.objects.filter(batchno = activebatchno, status = None).order_by('createdon').last()
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
                    # save register history
                    obj = Register.objects.filter(
                        batchno=activebatchno).order_by('createdon').last()
                    obj2 = RegisterHistory(
                        product=obj.product,
                        batchno=obj.batchno,
                        boxno=obj.boxno,
                        status=obj.status,
                        createdon=obj.createdon,
                        updatedon=obj.updatedon,
                        weight=obj.weight,
                        operator=obj.operator,
                        petugasgudang=obj.petugasgudang,
                        createdby=obj.createdby,
                        updatedby=obj.updatedby,
                        printedon=obj.printedon,
                        action="insert"
                    )
                    obj2.save()

                    config = AdminConfig.objects.first()
                    config.spvapproval = False
                    config.save()
                    # if weight.status == 3:
                    #     run_conveyor()
        return JsonResponse(data, safe=False, status=200)

@login_required(login_url=loginpage)
# @allowed_check(feature_alias='masterproduct')
def ReprintView(request):
    context = {}
    context['action'] = 'view'
    context['data'] = ReprintList.objects.all().order_by('-id')[:2]
    if request.method == "POST":
        form = ReprintForm(request.POST)
        context['form'] = form
        if form.is_valid():
            qr = form.cleaned_data.get('qr').split('|')
            productid = Product.objects.filter(code=qr[0]).first()
            if productid:
                register = Register.objects.filter(product=productid, batchno=qr[1], boxno=qr[2]).last()
                if register:
                    reprint = ReprintList(register=register)
                    reprint.save()
                    relay_on()
                else:
                    messages.error(request, 'Box tidak ditemukan.')
            else:
                messages.error(request, 'Box tidak ditemukan.')
            return redirect('reprint')
    else:
        context['form'] = ReprintForm()

    return render(request, 'reprint.html', context=context)

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
            # if str.__contains__(group, 'supervisor'):
            if str.__contains__(group, 'supervisor') or str.__contains__(group, 'administrator'):
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

@csrf_exempt
def SetOperator(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')

        print(json.loads(body_unicode))
        body = json.loads(body_unicode)
        operator1 = body['operator1']
        operator2 = body['operator2']

        config = AdminConfig.objects.first()
        config.operator = operator1.title()
        config.petugasgudang = operator2.title()
        config.save()
        if (not operator1) or (not operator2):
            return JsonResponse({"message": "Isikan nama operator terlebih dahulu."}, status=400)
        else:
            return JsonResponse({"message": "Operator berhasil ditambahkan."}, status=200)

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
        p.minweight cur_minweight, p.standardweight cur_standardweight, p.jumlahkoli, \
        case when p.code is null then \'New Data\'\
        when t.name <> p.name or t.maxweight <> p.maxweight or t.minweight <> p.minweight or t.standardweight <> p.standardweight or t.jumlahkoli <> p.jumlahkoli \
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
            try:
                print(list(reader)[0][1])
            except:
                reader = csv.reader(StringIO(file), delimiter=';')
            next(reader) #skip header
            ProductUploadTemp.objects.all().delete()
            for row in reader:
                jumlahkoli = row[5]
                if jumlahkoli == '':
                    jumlahkoli = 0
                obj = ProductUploadTemp(code=row[0], name=row[1], minweight=row[2],
                                        maxweight=row[3], standardweight=row[4], jumlahkoli=jumlahkoli, createdby=request.user)
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
        t.minweight <> p.minweight or t.standardweight <> p.standardweight or t.jumlahkoli <> p.jumlahkoli')

    for item in data:
        p = Product.objects.filter(code=item.code).first()
        if p:
            h = ProductHistory(code=p.code, name=p.name, maxweight=p.maxweight, minweight=p.minweight, standardweight=p.standardweight, jumlahkoli=p.jumlahkoli,
                            createdon=p.createdon, updatedon=p.updatedon, status=p.status, createdby=p.createdby, updatedby=p.updatedby)
            h.save()
        obj, created = Product.objects.update_or_create(
            code=item.code,
            defaults={'name': item.name, 'maxweight': item.maxweight,
                      'minweight': item.minweight, 'standardweight': item.standardweight, 'jumlahkoli':item.jumlahkoli, 'createdby': request.user},
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
    writer.writerow(['Code', 'Product Name', 'Min. Weight (gram)', 'Max. Weight (gram)', 'Std. Weight (gram)', 'Jumlah Koli'])
    for record in query_set:
        output.append([record.code, record.name,
                      record.minweight, record.maxweight, record.standardweight, record.jumlahkoli])
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
            obj.jumlahkoli = form.cleaned_data.get('jumlahkoli')
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
    context['message'] = ''

    if request.method == "POST":
        form = ReportBodyForm(request.POST)
        context['form'] = form
        if form.is_valid():
            # instance = form.save(commit=False)
            batchnoid = request.POST.get('batchno')
            product = Product.objects.get(weighingstate__id=batchnoid)
            batchno = WeighingState.objects.filter(id=batchnoid).values('batchno').first()['batchno']
            print(batchno)
            # reporttitle = ReportTitle.objects.get(id=request.POST.get('reporttitle'))
            # department = Department.objects.get(id=request.POST.get('department'))
            reporttitle = AdminConfig.objects.first().pdf_reporttitle
            department = AdminConfig.objects.first().pdf_department
            reviewdate = AdminConfig.objects.first().pdf_will_be_reviewed_value
            effectivedate = AdminConfig.objects.first().pdf_eff_date_value
            dnno = AdminConfig.objects.first().pdf_dn_value
            dnrev = AdminConfig.objects.first().pdf_rev_of_dn_value
            # reviewdate = request.POST.get('reviewdate')
            # effectivedate = request.POST.get('effectivedate')
            # dnno = request.POST.get('dnno')
            prevreportexist = ReportRegister.objects.filter(batchno=batchno, product=product).exists()
            
            # autonumber dnrev
            # dnrev = 0
            # if prevreportexist:
            #     dnrev = Report.objects.filter(batchno=batchno, product=product).values('dnrev').order_by('-dnrev').first()['dnrev']
            # dnrev = dnrev+1
            
            # manual dnrev
            # dnrev = request.POST.get('dnrev')
            signingdate = request.POST.get('signingdate')
            
            obj = Report(product=product, batchno=batchno, reporttitle=reporttitle, department=department,
                   reviewdate=reviewdate, effectivedate=effectivedate, dnno=dnno, dnrev=dnrev, signingdate=signingdate)
            obj.save()

            reportobj = Report.objects.last()
            data = Register.objects.filter(batchno=reportobj.batchno, product=reportobj.product)
            for row in data:
                obj = ReportRegister(report=reportobj, dnrev=reportobj.dnrev, product=row.product, batchno=row.batchno, \
                boxno=row.boxno, status=row.status, createdon=row.createdon, weight=row.weight, createdby=row.createdby, operator=row.operator, petugasgudang=row.petugasgudang)
                obj.save()
            return redirect('viewreportbody')
    else:
        reporttitle = AdminConfig.objects.first().pdf_reporttitle
        department = AdminConfig.objects.first().pdf_department
        if not reporttitle or not department:
            context['form'] = None
            context['message'] = 'Isikan Report Title & Department terlebih dahulu di menu Configuration!'
        else:
            context['form'] = list(ReportBodyForm())

    return render(request, 'report_body.html', context=context)


@login_required(login_url=loginpage)
@allowed_check(feature_alias='deletereportpdf')
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
    datamodel = RegisterHistory.objects.annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date', 'status', 'operator', 'petugasgudang','action').order_by('-input_date')
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
    datamodel = Register.objects.all()\
        .annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date','status', 'operator', 'petugasgudang').order_by('-input_date')
    hasFilter = False
    group = request.user.groups.all()[0].name
    if group != 'administrator':
        datamodel = datamodel.filter(Q(status=1) | Q(status=3))
    if request.method == "POST":
        form = ReportBatchForm(request.POST)
        product = request.POST.get('productid')
        batchno = request.POST.get('batchno')
        inputdatefrom = request.POST.get('inputdatefrom')
        inputdateto = request.POST.get('inputdateto')
        reporttype = request.POST.get('reporttype')
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
        if reporttype == '1':
            datamodel = datamodel.filter(Q(status=1) | Q(status=3))
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
        if reporttype == '1':
            datamodel = datamodel.filter(Q(status=1) | Q(status=3))
        if product or batchno or inputdatefrom or inputdateto or reporttype:
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
    writer.writerow(['Product Name', 'Batch No', 'Box No', 'Weight', 'Status', 'Date', 'Operator', 'Petugas Gudang'])
    for record in query_set:
        status = "Belum Ditimbang"
        if record.status == 1:
            status = "OK"
        elif record.status == 2:
            status = "Reject"
        elif record.status == 3:
            status = "Last Box"
        output.append([record.product_name, record.batchno,
                      record.boxno, record.iot_weight, status, record.input_date, record.operator, record.petugasgudang])
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
    # from weasyprint import HTML

    
    # datamodel = Register.objects.order_by('boxno')
    datamodel = ReportRegister.objects.order_by('boxno')
    datamodel2 = UploadedRegister.objects.order_by('boxno')
    config = AdminConfig.objects.all().first()
    group = request.user.groups.all()[0].name
    if group != 'administrator':
        datamodel = datamodel.filter(Q(status=1) | Q(status=3))

    product_name = ""
    if request.method == "GET":
        form = ReportBatchForm(request.GET)
        product = request.GET.get('productid')
        reportid = request.GET.get('id')
        header = Report.objects.all().get(id=reportid)
        # datamodel = datamodel.filter(batchno=header.batchno, product=header.product)
        datamodel = datamodel.filter(report = header).filter(Q(status=1) | Q(status=3)).order_by('boxno')
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
    return render(request, 'report_batch_pdf_template2.html', context={'data': datamodel, 'data2': datamodel2, 'header': header, 'config':config,'rowlen': rowlen, 'signature':signature})
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
        form.fields["operator"].queryset = User.objects.filter(groups__name='operator')
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
        form.fields["operator"].queryset = User.objects.filter(groups__name='operator')
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
    # context['data'] = WeighingState.objects.all()
    context['data'] = WeighingState.objects.raw('SELECT t.*, ifnull(koli_register,0) koli_register  \
        FROM mainApp_weighingstate t \
        left join ( select product_id, batchno, count(*) koli_register from mainApp_register \
        where status = 1 or status = 3 group by product_id, batchno) \
         r on t.product_id = r.product_id and \
        t.batchno = r.batchno')
    if request.method == "POST":
        privilegecheck = allowed_check_function('managebatch',request)
        print(privilegecheck)
        if privilegecheck:
            form = WeighingStateInitialForm(request.POST)
            form.fields["operator"].queryset = User.objects.filter(groups__name='operator')
            context['form'] = form
            if form.is_valid():
                instance = form.save(commit=False)
                instance.pendingstatus = True
                instance.status = False
                productid = form.cleaned_data.get('product').id
                instance.jumlahkoli = Product.objects.filter(id=productid).last().jumlahkoli
                instance.batchno = form.cleaned_data.get('batchno').upper()
                # batchnoobj = WeighingState.objects.all()
                # batchnoobj.update(status=False)
                instance.save()
                return redirect('viewweighingstate')
        else:
            return HttpResponse('Anda tidak diizinkan untuk melihat halaman ini. <a href="javascript:history.go(-1)" class="btn btn-default">Kembali</a>')
    else:
        form = WeighingStateInitialForm()
        form.fields["operator"].queryset = User.objects.filter(groups__name='operator')
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
    # context['data'] = WeighingState.objects.all()
    context['data'] = WeighingState.objects.raw('SELECT t.*, ifnull(koli_register,0) koli_register  \
        FROM mainApp_weighingstate t \
        left join ( select product_id, batchno, count(*) koli_register from mainApp_register \
        where status = 1 or status = 3 group by product_id, batchno) \
         r on t.product_id = r.product_id and \
        t.batchno = r.batchno')
    if request.method == 'GET':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateForm(instance=obj)
        form.fields["operator"].queryset = User.objects.filter(groups__name='operator')
        context['form'] = list(form)
    if request.method == 'POST':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateForm(request.POST, instance=obj)
        form.fields["operator"].queryset = User.objects.filter(groups__name='operator')
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

        # if group == 'supervisorgudang':
        #     form.fields["spvgudang"].queryset = User.objects.filter(
        #         id = request.user.id)
        # elif group == 'supervisorproduksi':
        #     form.fields["spvpabrik"].queryset = User.objects.filter(
        #         id=request.user.id)
        # elif group == 'administrator':
        #     form.fields["spvgudang"].queryset = User.objects.filter(
        #         groups__name='supervisorgudang')
        #     form.fields["spvpabrik"].queryset = User.objects.filter(
        #         groups__name='supervisorproduksi')

        context['data'] = WeighingState.objects.all()
        context['form'] = list(form)
    if request.method == 'POST':
        obj = WeighingState.objects.get(id=id)
        form = WeighingStateCloseForm(request.POST, user=request.user, instance=obj)
        # context['data'] = WeighingState.objects.all()
        context['data'] = WeighingState.objects.raw('SELECT t.*, ifnull(koli_register,0) koli_register  \
        FROM mainApp_weighingstate t \
        left join ( select product_id, batchno, count(*) koli_register from mainApp_register \
        where status = 1 or status = 3 group by product_id, batchno) \
         r on t.product_id = r.product_id and \
        t.batchno = r.batchno')
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
    datamodel = RegisterHistory.objects.filter(batchno=batchno).annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
        .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date', 'status','operator','petugasgudang').order_by('-input_date')
    # datamodel = RegisterHistory.objects.filter(batchno=batchno).filter(Q(status=1) | Q(status=3)).annotate(product_name=F('product__name'), iot_weight=F('weight'), input_date=F('createdon'))\
    #     .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight', 'input_date', 'status','operator','petugasgudang').order_by('-input_date')
    context['data'] = datamodel
    return render(request, 'batchno_history.html', context=context)

@login_required(login_url=loginpage)
@allowed_users(allowed_roles=['administrator'])
def viewConfig(request):
    context = {}
    obj = AdminConfig.objects.filter(pdf_reporttitle=None, pdf_department=None)
    obj.delete()
    obj = AdminConfig.objects.all().first()
    form = list(ConfigForm(instance=obj))
    halflen = -(len(form) // -2)
    context['form'] = form[:halflen]
    context['form2'] = form[halflen:]
    context['data'] = AdminConfig.objects.all()
    # context['data'] = obj
    if request.method == "POST":
        form = ConfigForm(request.POST, instance=obj)
        if form.is_valid():
            weightadjustment = form.cleaned_data.get('weightadjustment')
            if weightadjustment > 0.0005 or weightadjustment < 0:
                context['message'] = 'Perubahan harus diantara 0 - 0.0005.'    
            else:
                form.save()
                context['message'] = 'Data berhasil diubah.'
                return redirect('config')
    return render(request, 'config.html', context=context)

## printing
@csrf_exempt
def printWeightCurrentBox(request): #obsolete
    if request.method == "GET":
        batchno = request.GET.get('batchno')
        boxno = request.GET.get('boxno')
        productcode = request.GET.get('product')
        if boxno and batchno and productcode:
            data = list(Register.objects.filter(batchno=batchno, boxno=boxno, product__code=productcode).filter(Q(status=1) | Q(status=3)).values())
        elif not boxno and not batchno and not productcode:
            data = list(Register.objects.values().order_by('-id'))[0]
        else:
            data = list({"Complete batchno and boxno!"})
        return JsonResponse(data, safe=False, status=200)
    else:
        data = ['Wrong page!']
        return JsonResponse(data, safe=False, status=400)

## printing
@csrf_exempt
def getPrintData(request):
    if request.method == "GET":
        mode = request.GET.get('mode')
        if mode == 'reprint':
            data = list(ReprintList.objects.filter(status=0).values('register__weight').last())
        elif not boxno and not batchno and not productcode:
            data = list(Register.objects.values().order_by('-id'))[0]
        else:
            data = list({"Complete product code, batchno, boxno!"})
        return JsonResponse(data, safe=False, status=200)
    else:
        data = ['Wrong page!']
        return JsonResponse(data, safe=False, status=400)

## printing
@csrf_exempt
def runConveyorBC(request):
    if request.method == "GET":
        spvapproval = AdminConfig.objects.first().spvapproval
        msg = ''
        status = 200
        if spvapproval:
            result = run_conveyor()
            if result:
                msg = "Conveyor berjalan!"
            else:
                msg = "Conveyor tidak dapat berjalan!"
                status = 400
            data = [msg]

            config = AdminConfig.objects.first()
            config.spvapproval = False
            config.save()
        else:
            msg = "Aktifkan SPV Approval terlebih dahulu!"
            status = 400
            data = [msg]

        return JsonResponse(data, safe=False, status=status)
    else:
        data = ['Wrong page!']
        return JsonResponse(data, safe=False, status=400)


## relay
@csrf_exempt
def turn_relay_on(request):
    if request.method == "GET":
        # spvapproval = AdminConfig.objects.first().spvapproval
        # msg = ''
        # status = 200
        # if spvapproval:
        #     result = relay_on()
        #     if result:
        #         msg = "Relay On!"
        #     else:
        #         msg = "Relay tidak dapat berjalan!"
        #         status = 400
        #     data = [msg]

        #     config = AdminConfig.objects.first()
        #     config.spvapproval = False
        #     config.save()
        # else:
        #     msg = "Aktifkan SPV Approval terlebih dahulu!"
        #     status = 400
        #     data = [msg]
        msg = ''
        status = 200
        result = relay_on()
        if result:
            msg = "Relay On!"
        else:
            msg = "Relay tidak dapat berjalan!"
            status = 400
        data = [msg]
        return JsonResponse(data, safe=False, status=status)

        # return JsonResponse(data, safe=False, status=status)
    else:
        data = ['Wrong page!']
        return JsonResponse(data, safe=False, status=400)


@csrf_exempt
def turn_relay_off(request):
    if request.method == "GET":
        # spvapproval = AdminConfig.objects.first().spvapproval
        # msg = ''
        # status = 200
        # if spvapproval:
        #     result = relay_off()
        #     if result:
        #         msg = "Relay Off!"
        #     else:
        #         msg = "Relay tidak dapat berjalan!"
        #         status = 400
        #     data = [msg]

        #     config = AdminConfig.objects.first()
        #     config.spvapproval = False
        #     config.save()
        # else:
        #     msg = "Aktifkan SPV Approval terlebih dahulu!"
        #     status = 400
        #     data = [msg]
        msg = ''
        status = 200
        result = relay_off()
        if result:
            msg = "Relay Off!"
        else:
            msg = "Relay tidak dapat berjalan!"
            status = 400
        data = [msg]
        return JsonResponse(data, safe=False, status=status)
    else:
        data = ['Wrong page!']
        return JsonResponse(data, safe=False, status=400)
