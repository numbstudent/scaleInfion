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
def BatchView(request):
    if is_ajax(request) and request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"message": form.errors}, status=400)

    elif is_ajax(request) and request.method == "GET":
        data = Product.objects.all()
        response = serializers.serialize("json", data)
        return HttpResponse(response, content_type='application/json')


@csrf_exempt
def RegisterView(request, batchno=None):
    if is_ajax(request) and request.method == "POST":
        form = RegisterForm(request.POST)
        print(request.POST)
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
        if batchno:
            insertWeight(batchno)
            data = Register.objects.annotate(product_name=F('product__name'),iot_weight=F('weight__weighing'))\
            .values('id', 'batchno', 'boxno', 'product_name', 'iot_weight')\
            .filter(batchno=batchno).order_by('-createdon')
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
    b = Iot(lot='1', status='1', weighing=random.uniform(-10, 10))
    b.save()

    if request.method == "GET":
        data = Iot.objects.all().order_by('-datetime').values('id','weighing').first()
        return JsonResponse(data, safe=False, status=200)

def insertWeight(batchno):
    newweight = Iot.objects.all().order_by('-datetime').values_list('id', 'weighing')
    unweighted = Register.objects.filter(batchno=batchno, status=0)
    if newweight.exists() and unweighted.exists():
        if newweight.first()[1] > 0:
            weightid = newweight.first()[0]
            print(newweight)
            obj = unweighted.first()
            obj.status = 1
            obj.weight_id = weightid
            obj.save()