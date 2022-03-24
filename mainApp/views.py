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

loginpage = 'login'

@login_required(login_url=loginpage)
def index(request):
    return render(request, 'home.html')


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
            boxkosongexists = Register.objects.filter(product=productid, batchno=batchno, status=0).exists()
            if boxexists:
                return JsonResponse({"message": "Box sudah diinput. Hapus box terlebih dahulu untuk mereset."}, status=400)
            elif boxkosongexists:
                return JsonResponse({"message": "Box kosong harus ditimbang terlebih dahulu."}, status=400)
            else:
                instance = form.save(commit=False)
                instance.product = productid
                instance.save()
                # ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"message": "Data berhasil diinput"}, status=200)
        else:
            return JsonResponse({"message": "Isikan parameter."}, status=400)

    elif is_ajax(request) and request.method == "GET":
        batchno = request.GET.get('batchno')
        code = request.GET.get('code')
        if batchno:
            insertWeight(batchno)
            data = Register.objects.annotate(product_name=F('product__name'),iot_weight=F('weight__weighing'))\
            .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight')\
            .filter(batchno=batchno, product__code=code).order_by('-createdon')
        else:
            data = Register.objects.all().values()
        return JsonResponse(list(data), safe=False, status=200)

    elif is_ajax(request) and request.method == "PUT":
        body = json.loads(request.body)
        registerid = body['registerid']
        obj = Register.objects.filter(id=registerid)
        print(obj)
        obj.delete()
        return JsonResponse({"message": "Data berhasil dihapus"}, status=200)

@csrf_exempt
def ScaleView(request):
    #app_test
    import random
    b = Logging(lot='1', status='1', weighing=random.uniform(-10, 10))
    b.save()

    obj = Logging.objects.latest('id')
    print(obj)

    if request.method == "GET":
        data = Logging.objects.all().order_by('-id').values('id','weighing').first()
        return JsonResponse(data, safe=False, status=200)

def insertWeight(batchno):
    newweight = Logging.objects.all().order_by('-id').values_list('id', 'weighing')
    unweighted = Register.objects.filter(batchno=batchno, status=0)
    if newweight.exists() and unweighted.exists():
        if newweight.first()[1] > 0:
            weightid = newweight.first()[0]
            print(newweight)
            obj = unweighted.first()
            obj.status = 1
            obj.weight_id = weightid
            obj.save()


@login_required(login_url=loginpage)
def viewProduct(request):
    context = {}
    context['data'] = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        context['action'] = 'view'
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
    if request.method == 'GET':
        obj = Product.objects.get(id=id)
        form = ProductForm(instance=obj)
        context['data'] = Product.objects.all()
        context['form'] = form
    if request.method == 'POST':
        obj = Product.objects.filter(id=id).first()
        form = ProductForm(request.POST)
        context['data'] = obj
        context['form'] = form
        if form.is_valid():
            obj.name = form.cleaned_data.get('name')
            obj.code = form.cleaned_data.get('code')
            obj.status = form.cleaned_data.get('status')
            obj.save()
            return redirect('viewproduct')
    return render(request, 'master_product.html', context=context)
